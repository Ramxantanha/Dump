import os,platform
os.system("xdg-open https://www.facebook.com/677366316")
os.system('git pull')

trt=platform.architecture()[0]
if trt=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif trt=="64bit":
    __import__("dump")
