# http://www.cnblogs.com/wupeiqi/articles/5703697.html

import tornado.ioloop
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('t_ajax.html')
    def post(self):
        self.write('{"status": 1, "message": "ok"}')

class JAjaxHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('t_ajax2.html')
    def post(self):
        print(self.get_argument('k1'))
        self.write('{"status": 1, "message": "ok"}')

settings = {
    'template_path': 'views'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/ajax", JAjaxHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
