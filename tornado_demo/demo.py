# http://www.cnblogs.com/wupeiqi/articles/5341480.html

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        # self.render("xxx.html")  真实路径 ooo/xxx.html


settings = {
    'template_path': 'ooo',  # 存放网页的路径
    'static_path': 'zzz'     # 静态文件路径,一般存放css js
}


# 路由映射
application = tornado.web.Application([
    (r"/index", MainHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
