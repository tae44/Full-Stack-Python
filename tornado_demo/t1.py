import tornado.ioloop
import tornado.web
from tornado_demo.controllers import t1_home


settings = {
    'template_path': 'views',
    'static_path': 'statics'
}


# 路由映射
application = tornado.web.Application([
    (r"/index", t1_home.MainHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
