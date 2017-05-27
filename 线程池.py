import queue
import threading
import time
import contextlib

# 版本一
# class ThreadPool:
#
#     def __init__(self, maxnum=20):
#         self.queue = queue.Queue(maxsize=maxnum)
#         for i in range(maxnum):
#             self.queue.put(threading.Thread)
#
#     def getThread(self):
#         return self.queue.get()
#
#     def addThread(self):
#         self.queue.put(threading.Thread)
#
# pool = ThreadPool(10)
#
# def func(p, arg):
#     print(arg)
#     time.sleep(1)
#     p.addThread()
#
# for i in range(50):
#     thread = pool.getThread()
#     t = thread(target=func, args=(pool, i))
#     t.start()

# 版本二
StopEvent = object()

class ThreadPool:

    def __init__(self, max_num, max_task_num = None):
        if max_task_num:
            self.q = queue.Queue(max_task_num)
        else:
            self.q = queue.Queue()
        self.max_num = max_num
        self.cancel = False
        self.terminal = False
        self.generate_list = []
        self.free_list = []

    def run(self, func, args, callback=None):
        """
        线程池执行一个任务
        :param func: 任务函数
        :param args: 任务函数所需参数
        :param callback: 任务执行失败或成功后执行的回调函数
                        回调函数有两个参数1、任务函数执行状态；2、任务函数返回值（默认为None，即：不执行回调函数）
        :return: 如果线程池已经终止，则返回True否则None
        """
        if self.cancel:
            return
        if len(self.free_list) == 0 and len(self.generate_list) < self.max_num:
            pass