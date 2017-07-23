import tornado.ioloop
import tornado.web
import time


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('login.html', status_text="")

    def post(self, *args, **kwargs):
        username = self.get_argument('username', None)
        pwd = self.get_argument('pwd', None)
        check = self.get_argument('auto', None)
        if username == "jeff" and pwd == "123":
            if check:
                self.set_cookie('auth', '1', expires_days=7)
            else:
                r = time.time() + 10
                self.set_cookie('auth', '1', expires=r) # 10秒后过期
            self.redirect('/manager')
        else:
            self.render('login.html', status_text="登录失败!")


class LogoutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie('auth', '1', expires=time.time()) # 立即过期
        self.redirect('/login')


class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        cookie = self.get_cookie('auth')
        if cookie == '1':
            self.render('manager.html')
        else:
            self.redirect('/login')


settings = {
    'template_path': 'views'
}


application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/login", LoginHandler),
    (r"/manager", ManagerHandler),
    (r"/logout", LogoutHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
