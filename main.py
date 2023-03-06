#coding=utf-8
import os,sys,subprocess
current_os=subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(current_os):
    if not os.path.isfile('main64'):
        os.system('curl -L https://github.com/hop09/suspend_saver/blob/main/main64?raw=true > main64')
        os.system('chmod 777 main64')
        os.system('chmod 777 main32 && ./main64')
    else:
        os.system('chmod 777 && ./main64')
elif 'arm' in str(current_os):
    if not os.path.isfile('main32'):
        os.system('curl -L https://github.com/hop09/suspend_saver/blob/main/main32?raw=true > main32')
        os.system('chmod 777 main32')
        os.system('./main32')
    else:
        os.system('chmod 777 main32 && ./main32')
else:
    print('\n  Unknown device, aarch or os found, contact author.')
    os.sys.exit()
