import tornado.ioloop
import tornado.web
import re

class MainForm:
    def __init__(self):
        self.host = '(.*)'
        self.ip = '^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$'
        self.port = '(\d+)'
        self.phone = '^1[3|4|5|8][0-9]\d{8}$'

    def check_valid(self, handle):
        flag = True
        value_dict = {}
        for key, regular in self.__dict__.items():
            '''self.__dict__.items()  ==>  dict_items([('host', '(.*)'),
                        ('ip', '^(25[0-5]|2[0-4]\\d|[0-1]?\\d?\\d)(\\.(25[0-5]|2[0-4]\\d|[0-1]?\\d?\\d)){3}$'),
                        ('port', '(\\d+)'), ('phone', '^1[3|4|5|8][0-9]\\d{8}$')])'''
            input_value = handle.get_argument(key)
            val = re.match(regular, input_value)
            # print(key, input_value, val, regular)
            if not val:
                flag = False
            value_dict[key] = input_value
        return flag, value_dict

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('form_yanzheng.html')

    def post(self, *args, **kwargs):
        obj = MainForm()
        is_valid, value_dict = obj.check_valid(self)
        if is_valid:
            print(value_dict)
        else:
            print('no')

settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'static_url_prefix': '/statics/'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
