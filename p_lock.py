import threading
import time

# globals_num = 0
#
# lock = threading.RLock()
#
# def f():
#     lock.acquire()
#     global globals_num
#     globals_num += 1
#     time.sleep(0.5)
#     print(globals_num)
#     lock.release()
#
# for i in range(10):
#     t = threading.Thread(target=f)
#     t.start()

'''
    RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。
    如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire，必须调用n次的release才能真正释放所占用的琐。
'''
# lock = threading.Lock()
# lock.acquire()
# lock.acquire() # 产生了死琐
# lock.release()
# lock.release()

lock = threading.RLock()
lock.acquire()
lock.acquire() # 在同一线程内，程序不会堵塞
lock.release()
lock.release()
