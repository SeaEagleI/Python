#TextProBar.py
#coding:utf-8
from math import ceil
import time
scale = 50
def f(x):
    x = x/scale
    f = ((1+x)/2)**8
    return ceil(f*scale)

start = time.perf_counter()
for i in range(scale+1):
    fi = f(i)
    a = '*' * fi
    b = '.' * (scale-fi)
    c = (fi/scale)*100
    dur = time.perf_counter() - start
    if fi<= scale-2:
        print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    else:
        print("\r{:^3.0f}%[{}{}]{:.2f}s".format(c,a+'*'*2,b,dur),end="")
    time.sleep(0.1)
print("")

#print("执行开始".center(scale//2,"-"))
#print("\n"+"执行结束".center(scale//2,"-"))






















