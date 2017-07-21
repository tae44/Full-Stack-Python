from greenlet import greenlet
import gevent
import requests

# def a():
#     print('12')
#     gr2.switch()
#     print('34')
#     gr2.switch()
#
# def b():
#     print('56')
#     gr1.switch()
#     print('78')
#
# gr1 = greenlet(a)
# gr2 = greenlet(b)
# gr1.switch()

# def foo():
#     print('1-Running in foo')
#     gevent.sleep(2) # 切换到下一协程
#     print('2-Explicit context switch to foo again')
#
# def bar():
#     print('3-Explicit context to bar')
#     gevent.sleep(2)
#     print('4-Implicit context switch back to bar')
#
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar)
# ])

def f(url):
    print('GET: {}'.format(url))
    resp = requests.get(url)
    data = resp.text
    print(len(data))

gevent.joinall([
    gevent.spawn(f, 'https://www.python.org'),
    gevent.spawn(f, 'https://www.baidu.com'),
    gevent.spawn(f, 'https://github.com')
])
