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

inputs = [sk1] # 需要被监听的对象
outputs = [] # 回复消息的列表
message_dict = {} # 存放哪个客户端发送哪些消息

while True:
    # 有变化加入的,写什么加入什么,有错误加入的,相隔时间
    r_list, w_list, e_list = select.select(inputs, outputs, inputs, 1)
    print('正在监听的socket对象{}'.format(len(inputs)))
    print(r_list)
    for sk_or_conn in r_list:
        if sk_or_conn == sk1:
            # 表示有新用户连接
            conn, address = sk_or_conn.accept()
            inputs.append(conn)
            message_dict[conn] = []
        else:
            # 有老用户发消息
            try:
                data = str(sk_or_conn.recv(1024), encoding='utf-8')
            except Exception as e:
                inputs.remove(sk_or_conn)
            else:
                message_dict[sk_or_conn].append(data)
                outputs.append(sk_or_conn)

    for conn in w_list:
        message = message_dict[conn][0]
        conn.sendall(bytes(message.upper(), encoding='utf-8'))
        del message_dict[conn][0]
        outputs.remove(conn)

    # for sk in e_list:
    #     inputs.remove(sk)
