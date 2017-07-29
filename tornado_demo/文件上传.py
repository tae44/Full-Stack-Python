import tornado.ioloop
import tornado.web
import os

IMG_LIST = []

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('upfile.html', img_list = IMG_LIST)

    def post(self, *args, **kwargs):
        # print(self.get_argument('user'))
        # print(self.get_arguments('favor'))
        file_metas = self.request.files['fafafa']
        for meta in file_metas:
            # 要上传的文件名
            file_name = meta['filename']
            with open(os.path.join('statics', 'img', file_name), 'wb') as f:
                f.write(meta['body'])
            IMG_LIST.append(file_name)
        self.redirect('/index')

class XhrHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('ajax_upfile.html', img_list = IMG_LIST)

    def post(self, *args, **kwargs):
        file_metas = self.request.files['fafafa']
        for meta in file_metas:
            file_name = meta['filename']
            with open(os.path.join('statics', 'img', file_name), 'wb') as f:
                f.write(meta['body'])
            IMG_LIST.append(file_name)
        self.redirect('/xhr')

class JqHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('jquary_upfile.html', img_list = IMG_LIST)

    def post(self, *args, **kwargs):
        file_metas = self.request.files['fafafa']
        for meta in file_metas:
            file_name = meta['filename']
            with open(os.path.join('statics', 'img', file_name), 'wb') as f:
                f.write(meta['body'])
            IMG_LIST.append(file_name)
        self.redirect('/jq')

settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'static_url_prefix': '/statics/' # windows下貌似不用加,mac下面必须加
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/xhr", XhrHandler),
    (r"/jq", JqHandler)
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
