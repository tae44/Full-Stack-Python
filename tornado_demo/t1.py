import tornado.ioloop
import tornado.web

INPUT_LIST = []

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('t1.html', items=INPUT_LIST)
    def post(self):
        name = self.get_argument('xxx')
        INPUT_LIST.append(name)
        self.render('t1.html', items=INPUT_LIST)


settings = {
    'template_path': 'views',
    'static_path': 'statics'
}


# 路由映射
application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8800)
    tornado.ioloop.IOLoop.instance().start()
