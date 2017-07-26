import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        pass

class ManagerHandler(tornado.web.RequestHandler):
    def get(self):
        pass

settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'cookie_secret': 'abcd1234'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/manager", ManagerHandler)
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
