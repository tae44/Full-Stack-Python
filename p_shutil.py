import shutil
import os

os.chdir(r'C:\Users\syjiang\Desktop')

# shutil.copyfileobj(open('1.txt', 'r'), open('2.txt', 'w'))

# shutil.copyfile('1.txt', '2.txt')

# shutil.copymode('1.txt', '2.txt')

# shutil.copystat('1.txt', '2.txt')

# shutil.copy('1.txt', '2.txt')

# shutil.copytree('1', '3', ignore=shutil.ignore_patterns('*.txt'))

# shutil.rmtree('1')

shutil.move('1', '2')
