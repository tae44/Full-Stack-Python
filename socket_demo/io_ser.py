import socket
import select

sk1 = socket.socket()
sk1.bind(('127.0.0.1', 8001))
sk1.listen()

sk2 = socket.socket()
sk2.bind(('127.0.0.1', 8002))
sk2.listen()

sk3 = socket.socket()
sk3.bind(('127.0.0.1', 8003))
sk3.listen()

s = [sk1, sk2, sk3]
while True:
    r_list, w_list, e_list = select.select(s, [], [], 1)
    print(r_list)
    for sk in r_list:
        conn, address = sk.accept()
        conn.sendall(bytes('hello', encoding='utf-8'))
        conn.close()
