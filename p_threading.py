import threading
import time

# def p(x):
#     time.sleep(1)
#     print(x)
#
# for i in range(10):
#     p(i)
#
# for i in range(10):
#     t = threading.Thread(target=p, args=(i,))
#     t.start()

def a():
    print('start a')
    time.sleep(3)
    b()

def b():
    print('start b')

t1 = threading.Thread(target=a)
# t1.setDaemon(True) # 为True时主线程不等子线程退出再退出,默认FALSE
t1.start()
t1.join() # 等子线程结束再往下执行,不再并发执行

t2 = threading.Thread(target=a)
# t2.setDaemon(True)
t2.start()
t2.join(2) # 最多等2秒

t3 = threading.Thread(target=a)
# t3.setDaemon(True)
t3.start()
