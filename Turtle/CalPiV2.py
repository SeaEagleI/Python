#coding:utf-8
#CalPiV2.py
from random import random
from time import perf_counter

DARTS = 1000*1000*10
hits = 0.0
start = perf_counter()
for i in range(DARTS+1):
    x,y = random(),random()
    dist = pow(x**2+y**2,0.5)
    if dist <= 1.0:
        hits = hits + 1

pi = 4*(hits/DARTS)
print("pi = {}".format(pi))
print("time = {:.5f}".format(perf_counter()-start))










