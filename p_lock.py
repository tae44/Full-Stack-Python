import threading
import time

globals_num = 0

lock = threading.RLock()

def f():
    lock.acquire()
    global globals_num
    globals_num += 1
    time.sleep(0.5)
    print(globals_num)
    lock.release()

for i in range(10):
    t = threading.Thread(target=f)
    t.start()
