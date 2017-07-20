from wsgiref.simple_server import make_server

def new():
    return 'new'

def index():
    return 'index'

URLS = {
    '/new': new,
    '/index': index
}

def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']
    if url in URLS:
        func = URLS[url]
        ret = func()
    else:
        ret = '404'
    return ret

if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    httpd.serve_forever()
