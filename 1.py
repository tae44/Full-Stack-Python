def login(username, password):
    with open('user.db', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            user_list = line.split('@')
            if username == user_list[0] and password == user_list[1]:
                return '登陆成功!'
        return '登陆失败!'

def zhuce(username, password):
    with open('user.db', 'a', encoding='utf-8') as f:
        temp = '\n' + username + '@' + password
        f.write(temp)

def user_exsit(username):
    with open('user.db', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            user_list = line.split('@')
            if username == user_list[0]:
                return True
        return False

def delete(username):
    with open('user.db', 'r+', encoding='utf-8') as f:
        for line in f:
            if line.startswith(username):
                
                return 'ok'
        return 'no'

def change_pwd(username, password):
    with open('user.db', 'r+', encoding='utf-8') as f:
        for line in f:
            print(line)

if __name__ == '__main__':
    print('欢迎登陆本系统!请输入序号操作: 1-->登陆  2-->注册  3-->删除  4-->修改密码')
    id = input('请输入序号: ')
    if id == '1':
        user = input('请输入用户名: ')
        pwd = input('请输入密码: ')
        print(login(user, pwd))
    elif id == '2':
        user = input('请输入用户名: ')
        pwd = input('请输入密码: ')
        ret = user_exsit(user)
        if ret:
            print('用户名已存在!')
        else:
            zhuce(user, pwd)
            print('注册成功!')
    elif id == '3':
        user = input('请输入用户名: ')
        print(delete(user))
    else:
        print('序号输入错误!')
