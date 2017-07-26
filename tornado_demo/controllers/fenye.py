import tornado.web

LIST_INFO = [
    {'username': 'jeff', 'email': '123@qq.com'}
]
# 生成测试数据
for i in range(300):
    temp = {'username': 'jeff' + str(i), 'email': str(i) + '123@qq.com'}
    LIST_INFO.append(temp)

class Pagination:
    def __init__(self, current_page, all_item):
        # 计算总页数,余数大于0则再加1页
        all_page, c = divmod(all_item, 5)
        if c > 0:
            all_page += 1
        self.all_page = all_page
        try:
            current_page = int(current_page)
        except:
            current_page = 1
        if current_page < 1:
            current_page = 1
        self.current_page = current_page

    @property
    def start(self):
        return (self.current_page - 1) * 5

    @property
    def end(self):
        return self.current_page * 5

    def page_str(self, base_url):
        list_page = []
        if self.all_page < 11:  # 总页数小于11,有多少显示多少
            s = 1  # 起始页数
            t = self.all_page  # 结束页数
        else:
            if self.current_page <= 6:  # 总页数大于11,点击页数小于6,不能显示出负数页码
                s = 1
                t = 11
            else:
                if self.current_page + 5 > self.all_page:  # 不能显示多余的页码
                    s = self.all_page - 10
                    t = self.all_page
                else:
                    s = self.current_page - 5  # 正常情况,显示当前点击页的前5页和后5页
                    t = self.current_page + 5
        first_page = '<a href="{}1">首页</a>'.format(base_url,)
        list_page.append(first_page)
        if self.current_page == 1:
            prev_page = '<a href="javascript:void(0)">上一页</a>'
        else:
            prev_page = '<a href="{}{}">上一页</a>'.format(base_url, self.current_page - 1)
        list_page.append(prev_page)
        for p in range(s, t + 1):
            if p == self.current_page:
                # 页码相同加样式
                temp = '<a class="active" href="{}{}">{}</a>'.format(base_url, p, p)
            else:
                temp = '<a href="{}{}">{}</a>'.format(base_url, p, p)
            list_page.append(temp)
        if self.current_page == self.all_page:
            next_page = '<a href="javascript:void(0)">下一页</a>'
        else:
            next_page = '<a href="{}{}">下一页</a>'.format(base_url, self.current_page + 1)
        list_page.append(next_page)
        last_page = '<a href="{}{}">尾页</a>'.format(base_url, self.all_page)
        list_page.append(last_page)
        # 页面跳转
        jump = '''<input type="text"><a onclick="Jump({}, this)">GO</a>'''.format(base_url,)
        script = '''
        <script>
            function Jump(baseUrl, arg) {
                var val = arg.previousElementSibling.value;
                if (val.trim().length > 0 && val > 0) {
                    location.href = baseUrl + val
                }
            }
        </script>
        '''
        list_page.append(jump)
        list_page.append(script)
        return "".join(list_page)

class MainHandler(tornado.web.RequestHandler):
    def get(self, page):
        page_obj = Pagination(page, len(LIST_INFO))
        current_list = LIST_INFO[page_obj.start:page_obj.end]
        str_page = page_obj.page_str('/index/')
        self.render('fenye.html', list_info = current_list, current_page = page_obj.current_page, str_page = str_page)

    def post(self, page):
        user = self.get_argument('username')
        email = self.get_argument('email')
        temp = {'username': user, 'email': email}
        LIST_INFO.append(temp)
        self.redirect('/index/' + page)

class IndexHandler(tornado.web.RequestHandler):
    def get(self, page):
        self.write('测试二级路由')
