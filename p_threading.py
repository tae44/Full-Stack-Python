import threading
import time

def p(x):
    time.sleep(1)
    print(x)

# for i in range(10):
#     p(i)

for i in range(10):
    t = threading.Thread(target=p, args=(i,))
    t.start()
