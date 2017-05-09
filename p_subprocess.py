import subprocess

# ret = subprocess.call(['ls', '-l'], shell=False)
# print(ret)

# ret = subprocess.call('ls -l', shell=True)
# print(ret)

# ret = subprocess.check_call('ls -l', shell=True)

# ret = subprocess.check_output('ls -l', shell=True)
# print(ret)

ret1 = subprocess.Popen(['mkdir', '/Users/jason/Desktop/t1'])
ret2 = subprocess.Popen('mkdir /Users/jason/Desktop/t2', shell=True)
subprocess.Popen('mkdir t3', shell=True, cwd='/Users/jason/Desktop')
