import hashlib
import pickle
import os
import subprocess


def register(user, pwd):
    if os.path.exists('user.db'):
        f = open('user.db', 'ab')
        f.write(b'\n')
    else:
        f = open('user.db', 'wb')
    content = '{} + @ + {}'.format(user, pwd)
    hash = hashlib.md5(b'asdfghj')
    hash.update(bytes(content, encoding='utf-8'))
    content = hash.hexdigest()
    pickle.dump(content, f)
    f.close()


def login(user, pwd):
    f = open('user.db', 'rb')
    content = '{} + @ + {}'.format(user, pwd)
    hash = hashlib.md5(b'asdfghj')
    hash.update(bytes(content, encoding='utf-8'))
    content = hash.hexdigest()
    account_info = pickle.load(f)
    if content != account_info:
        return True
    return False


def main(data):
    user = input('请输入登录名: ')
    pwd = input('请输入密码: ')
    if data == 'register':
        register(user, pwd)
    elif data == 'login':
        ret = login(user, pwd)
        return ret


def run_com(command):
    return subprocess.check_output('{}'.format(command), shell=True)
