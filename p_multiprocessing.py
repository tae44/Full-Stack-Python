from multiprocessing import Process, Value, Array, Manager
import time

# def f(name):
#     print('hello', name)
#     time.sleep(1)
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = Process(target=f, args=('bob',))
#         p.start()
#         # p.join()

# 进程之间不共享数据

# li = []
#
# def foo(i):
#     li.append(i)
#     print('say hi', li)
#
# if __name__ == '__main__':
#     for i in range(10):
#         p = Process(target=foo, args=(i,))
#         p.start()

# 在使用并发设计的时候最好尽可能的避免共享数据，尤其是在使用多进程的时候。如果你真有需要共享数据，multiprocessing提供了两种方式。

# Shared memory
# def f(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]
#
# if __name__ == '__main__':
#     num = Value('d', 0.0)
#     arr = Array('i', range(10))
#
#     p = Process(target=f, args=(num, arr))
#     p.start()
#     p.join()
#
#     print(num.value)
#     print(arr[:])

# Server process
# def f(d, l):
#     d[1] = '1'
#     d['2'] = 2
#     d[0.25] = None
#     l.reverse()
#
# if __name__ == '__main__':
#     with Manager() as manager:
#         d = manager.dict()
#         l = manager.list(range(10))
#
#         p = Process(target=f, args=(d, l))
#         p.start()
#         p.join()
#
#         print(d)
#         print(l)

def f(i, dic):
    dic[i] = 100 + i
    print(len(dic))

if __name__ == '__main__':
    m = Manager()
    dic = m.dict()
    # dic = {}

    for i in range(10):
        p = Process(target=f, args=(i, dic))
        p.start()
        # p.join()
        time.sleep(1)
