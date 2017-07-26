import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        print(self.cookies)
        self.set_cookie('k1', '88')
        print(self.get_cookie('k1'))
        self.render('t_cookie2.html')

settings = {
    'template_path': 'views',
    'static_path': 'statics'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
