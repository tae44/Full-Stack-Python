import queue
import threading
import time

class ThreadPool:

    def __init__(self, maxnum=20):
        self.queue = queue.Queue(maxsize=maxnum)
        for i in range(maxnum):
            self.queue.put(threading.Thread)

    def getThread(self):
        return self.queue.get()

    def addThread(self):
        self.queue.put(threading.Thread)

pool = ThreadPool(10)

def func(p, arg):
    print(arg)
    time.sleep(1)
    p.addThread()

for i in range(50):
    thread = pool.getThread()
    t = thread(target=func, args=(pool, i))
    t.start()
