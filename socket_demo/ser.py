import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9999))
sk.listen(2) # 最大监听
while True:
    conn, address = sk.accept()
    conn.sendall(bytes('hello world', encoding='utf-8'))
    while True:
        ret_bytes = conn.recv(1024)
        ret_str = str(ret_bytes, encoding='utf-8')
        if ret_str == 'q':
            break
        conn.sendall(bytes(ret_str.upper(), encoding='utf-8'))
    # print(conn)
    # print(address)
