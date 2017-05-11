import shutil
import os
import zipfile
import tarfile

# os.chdir(r'C:\Users\syjiang\Desktop')

# shutil.copyfileobj(open('1.txt', 'r'), open('2.txt', 'w'))

# shutil.copyfile('1.txt', '2.txt')

# shutil.copymode('1.txt', '2.txt')

# shutil.copystat('1.txt', '2.txt')

# shutil.copy('1.txt', '2.txt')

# shutil.copytree('1', '3', ignore=shutil.ignore_patterns('*.txt'))

# shutil.rmtree('1')

# shutil.move('1', '2')

# ret = shutil.make_archive('/Users/jason/Desktop/www', 'gztar', root_dir='/Users/jason/Desktop/111')

z = zipfile.ZipFile('/Users/jason/Desktop/1112.zip', 'w')
z.write('/Users/jason/Desktop/111')
z.close()
