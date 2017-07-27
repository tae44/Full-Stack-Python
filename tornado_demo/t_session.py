import tornado.ioloop
import tornado.web
import hashlib
import time

container = {} # 存放session的字典,随机字符串+用户信息字典

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('t_session.html')

    def post(self):
        if self.get_argument('username', None) in ['jeff', 'jason']:
            obj = hashlib.md5()
            obj.update(bytes(str(time.time()), encoding='utf-8')) # 用当前时间戳生成加密字符串
            random_str = obj.hexdigest()
            container[random_str] = {}
            container[random_str]['k1'] = 'Hello'  # 加密字符串对应用户信息的字典
            container[random_str]['k2'] = self.get_argument('username', None) + ' World'
            container[random_str]['is_login'] = True
            self.set_cookie('cc', random_str)      # 将cookie写入浏览器
            self.redirect('/manager')
        else:
            self.redirect('/index')

class ManagerHandler(tornado.web.RequestHandler):
    def get(self):
        random_str = self.get_cookie('cc')         # 取出cookie对应的加密字符串
        current_userInfo = container.get(random_str, None)
        if not current_userInfo:
            self.redirect('/index')
        else:
            if current_userInfo.get('is_login', None):
                temp = '{} - {}'.format(current_userInfo.get('k1', ''), current_userInfo.get('k2', ''))
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
