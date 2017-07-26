import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_argument('u', None) in ['jeff', 'jason']:
            # self.set_cookie('name', self.get_argument('u'))
            self.set_secure_cookie('name', self.get_argument('u'))
            self.write('登录成功')
        else:
            self.write('请登录')

class ManagerHandler(tornado.web.RequestHandler):
    def get(self):
        # if self.get_cookie('name', None) in ['jeff', 'jason']:
        if str(self.get_secure_cookie('name', None), encoding='utf-8') in ['jeff', 'jason']:
            self.write('欢迎你! ' + str(self.get_secure_cookie('name')))
        else:
            self.redirect('/index')

settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'cookie_secret': 'abcd1234'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),      # http://127.0.0.1:8888/index?u=jason
    (r"/manager", ManagerHandler),  # http://127.0.0.1:8888/manager
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
