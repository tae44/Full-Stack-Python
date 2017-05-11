import subprocess

# ret = subprocess.call(['ls', '-l'], shell=False)
# print(ret)

# ret = subprocess.call('ls -l', shell=True)
# print(ret)

# ret = subprocess.check_call('ls -l', shell=True)

# ret = subprocess.check_output('ls -l', shell=True)
# print(ret)

# ret1 = subprocess.Popen(['mkdir', '/Users/jason/Desktop/t1'])
# ret2 = subprocess.Popen('mkdir /Users/jason/Desktop/t2', shell=True)
# subprocess.Popen('mkdir t3', shell=True, cwd='/Users/jason/Desktop')

obj = subprocess.Popen(['python'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
obj.stdin.write('print(1)\n')
obj.stdin.write('print(2)')
obj.stdin.close()

cmd_out = obj.stdout.read()
obj.stdout.close()
cmd_error = obj.stderr.read()
obj.stderr.close()

print(cmd_out)
print(cmd_error)
