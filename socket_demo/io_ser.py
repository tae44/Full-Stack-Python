import socket
import select

sk1 = socket.socket()
sk1.bind(('127.0.0.1', 8001))
sk1.listen()

# sk2 = socket.socket()
# sk2.bind(('127.0.0.1', 8002))
# sk2.listen()
#
# sk3 = socket.socket()
# sk3.bind(('127.0.0.1', 8003))
# sk3.listen()

s = [sk1]
while True:
    r_list, w_list, e_list = select.select(s, [], s, 1)
    print('正在监听的socket对象{}'.format(len(s)))
    print(r_list)
    for sk_or_conn in r_list:
        if sk_or_conn == sk1:
            # 表示有新用户连接
            conn, address = sk_or_conn.accept()
            s.append(conn)
        else:
            # 有老用户发消息
            try:
                data = str(sk_or_conn.recv(1024), encoding='utf-8')
                sk_or_conn.sendall(bytes(data.upper(), encoding='utf-8'))
            except Exception as e:
                s.remove(sk_or_conn)

    # for sk in e_list:
    #     s.remove(sk)
