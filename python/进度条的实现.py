import os
import time
import sys

file_name = input('请输入要创建的文件名称: ')

file_path = '/Users/jason/Desktop/test/{}'.format(file_name)

if os.path.exists(file_path):
    print('文件已存在!')
else:
    for i in range(1, 51):
        sys.stdout.write('\r')
        sys.stdout.write('{}% {}'.format(i*2, '#'*i))
        sys.stdout.flush()
        time.sleep(0.5)
    os.mkdir(file_path)
