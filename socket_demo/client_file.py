import socket
import os

obj = socket.socket()
obj.connect(('127.0.0.1', 9999))

# 发送文件大小
size = os.stat('testp.png').st_size
obj.sendall(bytes(str(size), encoding='utf-8'))

# 发送文件
with open('testp.png', 'rb') as f:
    for line in f:
        obj.sendall(line)

obj.close()
