import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8001))
data = str(obj.recv(1024), encoding='utf-8')
print(data)
obj.close()
