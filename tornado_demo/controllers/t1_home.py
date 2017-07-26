import tornado.web

INPUT_LIST = []

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('t1.html', items=INPUT_LIST)
    def post(self):
        name = self.get_argument('xxx')
        INPUT_LIST.append(name)
        self.render('t1.html', items=INPUT_LIST)
