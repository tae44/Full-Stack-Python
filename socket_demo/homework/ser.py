import socketserver
import user


class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        # 发送一级菜单
        conn = self.request
        conn.sendall(bytes('1: 注册  2: 登录  你的选择是: ', encoding='utf-8'))
        data = str(conn.recv(1024), encoding='utf-8')
        if data == '1':
            conn.sendall(bytes('register', encoding='utf-8'))
        elif data == '2':
            conn.sendall(bytes('login', encoding='utf-8'))
        conn.recv(1024)

        # 发送二级菜单
        conn.sendall(bytes('1: 执行命令  2: 上传文件  你的选择是: ', encoding='utf-8'))
        data = str(conn.recv(1024), encoding='utf-8')
        if data == '1':
            conn.sendall(bytes('请输入命令: ', encoding='utf-8'))
        elif data == '2':
            conn.sendall(bytes('请输入要上传的文件路径: ', encoding='utf-8'))

        # 判断是命令还是上传
        data = str(conn.recv(1024), encoding='utf-8')
        if data == 'command':
            conn.sendall(bytes('ack', encoding='utf-8'))
            com = str(conn.recv(1024), encoding='utf-8')
            ret = user.run_com(com)
            conn.sendall(ret)
        else:
            conn.sendall(bytes('ack', encoding='utf-8'))
            size = str(conn.recv(1024), encoding='utf-8')
            total_size = int(size)
            has_recv = 0
            conn.sendall(bytes('ack', encoding='utf-8'))
            f = open('xxx.png', 'wb')
            while total_size != has_recv:
                data = conn.recv(1024)
                f.write(data)
                has_recv += len(data)


if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 8888), MyServer)
    server.serve_forever()
