import tornado.ioloop
import tornado.web
import hashlib
import time

container = {} # 存放session的字典,随机字符串+用户信息字典

class Session:
    def __init__(self, handler):
        self.handler = handler
        self.random_str = None

    def __create_random_str(self):
        obj = hashlib.md5()
        obj.update(bytes(str(time.time()), encoding='utf-8'))  # 用当前时间戳生成加密字符串
        random_str = obj.hexdigest()
        return random_str

    def __setitem__(self, key, value):
        if not self.random_str:
            random_str = self.handler.get_cookie('__kaka__')
            if not random_str:  # 如果没有随机码则生成
                random_str = self.__create_random_str()
                container[random_str] = {}
            elif random_str not in container.keys(): # 如果服务器端有而浏览器没有
                random_str = self.__create_random_str()
                container[random_str] = {}
            self.random_str = random_str
        container[self.random_str][key] = value
        self.handler.set_cookie('__kaka__', self.random_str)

    def __getitem__(self, key):
        random_str = self.handler.get_cookie('__kaka__')
        if not random_str:
            return None
        current_userInfo = container.get(random_str, None)
        if not current_userInfo:
            return None
        return current_userInfo.get(key, None)

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = Session(self)

class IndexHandler(BaseHandler):
    def get(self):
        self.render('t_session.html')

    def post(self):
        if self.get_argument('username', None) in ['jeff', 'jason']:
            self.session['is_login'] = True
            self.session['k1'] = 'Hello'
            self.session['k2'] = self.get_argument('username', None) + ' World'
            self.redirect('/manager')
        else:
            self.redirect('/index')

class ManagerHandler(BaseHandler):
    def get(self):
        if self.session['is_login']:
            temp = '{} {}'.format(self.session['k1'], self.session['k2'])
            self.write(temp)
        else:
            self.redirect('/index')

settings = {
    'template_path': 'views',
    'static_path': 'statics',
    # 'cookie_secret': 'abcd1234'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/manager", ManagerHandler)
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
