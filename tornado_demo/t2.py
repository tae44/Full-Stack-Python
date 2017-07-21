import tornado.ioloop
import tornado.web

EMAIL_LIST = []
PWD_LIST = []

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 1.打开t2.html,读取内容(包含特殊语法)
        # 2.读取items
        # 3.得到新字符串
        # 4.返回给用户
        self.render('t2.html', items=EMAIL_LIST)
    def post(self):
        name = self.get_argument('email')
        EMAIL_LIST.append(name)
        self.render('t2.html', items=EMAIL_LIST)


settings = {
    'template_path': 'views'
}


# 路由映射
application = tornado.web.Application([
    (r"/login", MainHandler),
], **settings)


if __name__ == "__main__":
    application.listen(8800)
    tornado.ioloop.IOLoop.instance().start()
