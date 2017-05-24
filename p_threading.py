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
    time.sleep(5)
    b()

def b():
    print('start b')

t = threading.Thread(target=a)
t.setDaemon(True) # 为True时主线程不等子线程退出再退出,默认FALSE
t.start()
t = threading.Thread(target=a)
t.setDaemon(True)
t.start()
t = threading.Thread(target=a)
t.setDaemon(True)
t.start()
