from multiprocessing import Pool, TimeoutError
import time
import os

# http://www.cnblogs.com/resn/p/5591419.html

# def myFun(i):
#     time.sleep(2)
#     return i + 100
#
# def end_call(arg):
#     print('end_call', arg)
#
# if __name__ == '__main__':
#     p = Pool(5)
#
#     for i in range(10):
#         p.apply_async(func=myFun, args=(i,), callback=end_call)
#
#     print('end')
#     p.close()
#     p.join()

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        print(pool.map(f, range(10)))

        for i in pool.imap_unordered(f, range(10)):
            print(i)

        res = pool.apply_async(f, (20,))
        print(res.get(timeout=1))

        res = pool.apply_async(os.getpid)
        print(res.get(timeout=1))

        multiple_results = [pool.apply_async(os.getpid) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        res = pool.apply_async(time.sleep, (5,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print('发现一个 multiprocessing.TimeoutError异常')

        print('目前池中还有其他的工作')

    print('Now the pool is closed and no longer available')
