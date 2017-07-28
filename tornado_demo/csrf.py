import tornado.ioloop
import tornado.web

class CsrfHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('csrf.html')

    def post(self):
        self.write('csrf.post')

settings = {
    'template_path': 'views',
    'static_path': 'statics',
    # 'static_url_prefix': '/sss/',
    'xsrf_cookies': True
}

application = tornado.web.Application([
    (r"/csrf", CsrfHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
