import socket
import user
import os
import sys
import time


# 先注册或者登录
cli = socket.socket()
cli.connect(('127.0.0.1', 8888))
data = str(cli.recv(1024), encoding='utf-8')
print(data)
inp = input('>>> ')
cli.sendall(bytes(inp, encoding='utf-8'))
data = str(cli.recv(1024), encoding='utf-8')
ret = user.main(data)
if ret:
    print('登录失败!')
    cli.close()
cli.sendall(bytes('ack', encoding='utf-8'))

# 执行命令或者上传
data = str(cli.recv(1024), encoding='utf-8')
print(data)
inp = input('>>> ')
cli.sendall(bytes(inp, encoding='utf-8'))
data = str(cli.recv(1024), encoding='utf-8')
if '命令' in data:
    cli.sendall(bytes('command', encoding='utf-8'))
    cli.recv(1024)
    inp = input('请输入命令: ')
    cli.sendall(bytes(inp, encoding='utf-8'))
    ret = str(cli.recv(1024), encoding='utf-8')
    print(ret)
else:
    cli.sendall(bytes('upload', encoding='utf-8'))
    cli.recv(1024)
    inp = input('请输入文件路径: ')
    if os.path.exists(inp):
        size = os.stat(inp).st_size
        cli.sendall(bytes(str(size), encoding='utf-8'))
        cli.recv(1024)
        f = open(inp, 'rb')
        for line in f:
            cli.sendall(line)
            percent = str(cli.recv(1024), encoding='utf-8')
            sys.stdout.write('\r')
            sys.stdout.write('{} %'.format(percent))
            sys.stdout.flush()
            time.sleep(0.2)
    else:
        print('文件不存在!')
        cli.close()

cli.close()
