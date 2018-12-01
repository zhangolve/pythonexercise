import os
import subprocess

value = 123
os.environ['var'] = str(value)
os.system('echo ljmall')
subprocess.call('cd ~/Desktop', shell=True)
subprocess.call('bash ./test.sh', shell=True)
subprocess.call('you-get https://www.bilibili.com/video/av36845037', shell=True)

