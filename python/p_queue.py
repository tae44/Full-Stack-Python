import queue
import threading

message_queue = queue.Queue(10)

def producer(i):
    print('queue put {}'.format(i))
    message_queue.put(i, block=True, timeout=2) # block:当队列满时是否阻塞  timeout:阻塞多久还满就报错

def consumer(i):
    msg = message_queue.get(block=True, timeout=2)
    print('queue get: {}'.format(msg))

for i in range(12):
    t = threading.Thread(target=producer, args=(i,))
    t.start()

for i in range(10):
    t = threading.Thread(target=consumer, args=(i,))
    t.start()
