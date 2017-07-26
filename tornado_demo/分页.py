import tornado.ioloop
import tornado.web
from tornado_demo.controllers import fenye


settings = {
    'template_path': 'views',
    'static_path': 'statics'
}


application = tornado.web.Application([
    # (r"/index/(?P<num>\d*)/(?P<nid>\d*)", fenye.MainHandler),
    # http://127.0.0.1:8888/index/123/456
    (r"/index/(?P<page>\d*)", fenye.MainHandler)
], **settings)


# 测试二级路由
application.add_handlers("second.jason.com$", [
    (r"/index/(?P<page>\d*)", fenye.IndexHandler)
])

# jason.com/index/
# second.jason.com/index/

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
