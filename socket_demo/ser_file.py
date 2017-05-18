import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9999))
sk.listen(2)

while True:
    conn, address = sk.accept()

    # 先接收文件大小
    file_size = str(conn.recv(1024), encoding='utf-8')
    conn.sendall(bytes('ack', encoding='utf-8')) # 发送ack给客户端
    total_size = int(file_size)
    has_recv = 0

    # 再接收文件
    f = open('newp.png', 'wb')
    while total_size != has_recv:
        data = conn.recv(1024)
        f.write(data)
        has_recv += len(data)
    f.close()
