#coding:utf-8
import re
path = "pi.txt"

def Read(path):
    txt = open(path).read()
    for ch in "\n ":
        txt = txt.replace(ch,'')
    reg = r'-{5}(.*?)-{5}'
    txt = re.sub(reg,'',txt)
    return txt
    
def CalDigit():
    txt = Read(path)
    for i in range(10):
        print("Count {}:{} times".format(i,txt.count(str(i))))

CalDigit()
























