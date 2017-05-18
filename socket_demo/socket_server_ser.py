import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall(bytes('Hello!', encoding='utf-8'))
        while True:
            content = str(conn.recv(1024), encoding='utf-8')
            if content == 'q':
                break
            conn.sendall(bytes(content.upper(), encoding='utf-8'))

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), MyServer)
    server.serve_forever()
