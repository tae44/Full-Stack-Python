# http://www.cnblogs.com/wupeiqi/articles/5702910.html

import tornado.ioloop
import tornado.web
import hashlib
import time
import io
import tornado_demo.check_code

container = {}

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

class LoginHandler(BaseHandler):
    def get(self):
        self.render('yzm.html', status='')

    def post(self):
        user = self.get_argument('user', None)
        pwd = self.get_argument('pwd', None)
        code = self.get_argument('code', None)
        check_code = self.session['CheckCode']
        if code.upper() == check_code.upper():
            self.write('验证码正确')
        else:
            self.render('yzm.html', status='验证码错误')

class CheckCodeHandler(BaseHandler):
    def get(self):
        # 生成图片并返回
        mstream = io.BytesIO()
        # 创建图片,并写入验证码
        img, code = tornado_demo.check_code.create_validate_code()
        # 将图片对象写入到mstream
        img.save(mstream, "GIF")
        # 为每个用户保存其验证码
        self.session['CheckCode'] = code
        self.write(mstream.getvalue())

settings = {
    'template_path': 'views',
    'static_path': 'statics',
}

application = tornado.web.Application([
    (r"/login", LoginHandler),
    (r"/check_code", CheckCodeHandler)
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
