import tornado.ioloop
import tornado.web
import re
import os

class IPFiled:
    # 匹配ip的正则表达式
    REGULAR = '^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$'

    def __init__(self, error_dict=None, required=True):
        self.error_dict = {}
        if error_dict:
            self.error_dict.update(error_dict)
        self.required = required
        self.error = None       # 错误信息
        self.is_valid = False   # 匹配格式是否正确
        self.value = None

    def validate(self, name, input_value):
        '''
        :param name: 字段名
        :param input_value: 用户表单中输入的内容
        :return:
        '''
        if not self.required: # 用户输入可以为空
            self.is_valid = True
            self.value = input_value
        else:
            if not input_value.strip(): # 用户输入为空
                if self.error_dict.get('required', None):
                    self.error = self.error_dict['required']
                else:
                    self.error = '{} is required.'.format(name)
            else:
                ret = re.match(IPFiled.REGULAR, input_value) # 输入不为空,判断ip格式
                if ret:
                    self.is_valid = True
                    # self.value = ret.group() 同下方代码
                    self.value = input_value
                else:
                    if self.error_dict.get('valid', None):
                        self.error = self.error_dict['valid']
                    else:
                        self.error = '{} is invalid'.format(name)

class StringFiled:
    REGULAR = '^(.*)$'

    def __init__(self, error_dict=None, required=True):
        self.error_dict = {}
        if error_dict:
            self.error_dict.update(error_dict)
        self.required = required
        self.error = None
        self.is_valid = False
        self.value = None

    def validate(self, name, input_value):
        if not self.required:
            self.is_valid = True
            self.value = input_value
        else:
            if not input_value.strip():
                if self.error_dict.get('required', None):
                    self.error = self.error_dict['required']
                else:
                    self.error = '{} is required.'.format(name)
            else:
                ret = re.match(IPFiled.REGULAR, input_value)
                if ret:
                    self.is_valid = True
                    self.value = input_value
                else:
                    if self.error_dict.get('valid', None):
                        self.error = self.error_dict['valid']
                    else:
                        self.error = '{} is invalid'.format(name)

class CheckBoxFiled:
    def __init__(self, error_dict=None, required=True):
        self.error_dict = {}
        if error_dict:
            self.error_dict.update(error_dict)
        self.required = required
        self.error = None       # 错误信息
        self.is_valid = False   # 匹配格式是否正确
        self.value = None

    def validate(self, name, input_value):
        if not self.required:
            self.is_valid = True
            self.value = input_value
        else:
            if not input_value:
                if self.error_dict.get('required', None):
                    self.error = self.error_dict['required']
                else:
                    self.error = '{} is required.'.format(name)
            else:
                self.is_valid = True
                self.value = input_value

class FileFiled:
    REGULAR = '^(\w+\.pdf)|(\w+\.mp3)|(\w+\.txt)$'

    def __init__(self, error_dict=None, required=True):
        self.error_dict = {}
        if error_dict:
            self.error_dict.update(error_dict)
        self.required = required
        self.error = None
        self.is_valid = True
        self.value = []
        self.name = None
        # self.success_file_name_list = []

    def validate(self, name, all_file_name_list):
        self.name = name
        if not self.required:
            self.is_valid = True
            self.value = all_file_name_list
        else:
            if not all_file_name_list:
                self.is_valid = False
                if self.error_dict.get('required', None):
                    self.error = self.error_dict['required']
                else:
                    self.error = '{} is required.'.format(name)
            else:
                for file_name in all_file_name_list:
                    ret = re.match(FileFiled.REGULAR, file_name)
                    if not ret:
                        self.is_valid = False
                        if self.error_dict.get('valid', None):
                            self.error = self.error_dict['valid']
                        else:
                            self.error = '{} is invalid'.format(name)
                        break
                    else:
                        self.value.append(file_name)

    def save(self, request, path=None):
        file_metas = request.files.get(self.name)
        temp_list = []
        for meta in file_metas:
            file_name = meta['filename']
            new_file_name = os.path.join(path, file_name)
            if file_name and file_name in self.value:
                temp_list.append(new_file_name)
                with open(new_file_name, 'wb') as f:
                    f.write(meta['body'])
        self.value = temp_list

class BaseForm:
    def check_valid(self, handle):
        flag = True
        success_value_dict = {}
        error_message_dict = {}
        for key, regular in self.__dict__.items():
            if type(regular) == CheckBoxFiled:
                input_value = handle.get_arguments(key)
            elif type(regular) == FileFiled:
                # 获取文件名
                file_list = handle.request.files.get(key)
                input_value = []
                for item in file_list:
                    input_value.append(item['filename'])
            else:
                input_value = handle.get_argument(key)
            # 将具体的验证放在对象中
            regular.validate(key, input_value)
            if regular.is_valid:
                success_value_dict[key] = regular.value
            else:
                error_message_dict[key] = regular.error
                flag = False
        return flag, success_value_dict, error_message_dict

class IndexForm(BaseForm):
    def __init__(self):
        self.host = '(.*)'
        self.ip = '^(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}$'
        self.port = '(\d+)'
        self.phone = '^1[3|4|5|8][0-9]\d{8}$'

class HomeForm(BaseForm):
    def __init__(self):
        self.ip = IPFiled(required=True)
        self.host = StringFiled(required=False)
        self.favor = CheckBoxFiled(required=True)
        self.fafafa = FileFiled(required=True)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('form_yanzheng.html')

    def post(self, *args, **kwargs):
        obj = IndexForm()
        is_valid, success_dict, error_dict = obj.check_valid(self)
        if is_valid:
            print(success_dict)

class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('home_yanzheng.html', errorInfo = None)

    def post(self, *args, **kwargs):
        obj = HomeForm()
        is_valid, success_dict, error_dict = obj.check_valid(self)
        if is_valid:
            print('success: ', success_dict)
            self.write('success')
            obj.fafafa.save(self.request)
        else:
            print('error: ', error_dict)
            self.render('home_yanzheng.html', errorInfo = error_dict)

settings = {
    'template_path': 'views',
    'static_path': 'statics',
    'static_url_prefix': '/statics/'
}

application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/home", HomeHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
