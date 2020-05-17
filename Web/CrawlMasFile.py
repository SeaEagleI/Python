#coding:utf-8
from contextlib import closing
from math import ceil
import os.path as op
import requests
import time,sys

dir_path = "/home/andrew/Downloads"
turns = 100
len_limit = 20
time_out = 3
manual = False
chunk,_1MB = 500*1024,1024*1024
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
           (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
M,T = [1024,'B','KB','MB','GB'],[60,'s','min','h','d']

def s(cells,box,shown=False):
    unit = box[0]
    if shown==False:
        for i in range(4):
            if cells<unit:
                return '{:.1f}'.format(cells)+box[i+1]
            cells = cells/unit
    else:
        tis = 0
        for i in range(4):
            if cells<unit:
                s = '{:.0f}'.format(cells)+box[i+1]+'{:.0f}'.format(tis)+box[i] if tis>1 else '{:.0f}'.format(cells)+box[i+1]
                break
            cells,tis = cells/unit,cells%unit
        return s

def Pro(cur,tot,start,last_t,scale=25,max_len=80):
    cur_t = time.perf_counter()
    count = ceil((cur/tot)*scale)
    a = '=' * count
    b = ' ' * (scale-count)
    c = (cur/tot)*100
    dur = cur_t-start
    sp = chunk/float(cur_t-last_t)
    rm = (tot-cur)/sp
    if count<=scale-1:
        fi,rm = '>',s(rm,T,True)
    else:
        fi,rm = '=',''
    line = "\r{}/{} {:.0f}%[{}{}{}] {} {} {}".format(s(cur,M),s(tot,M),c,a,fi,b,s(dur,T,True),s(sp,M)+'/s',rm)
    line += ' '*(max_len-len(line))
    print(line,end="")
    return cur_t

def Download(response,path,tot_size):
    with closing(response) as close:
        start = time.perf_counter()
        cur_size,last = 0,start
        with open(path,"wb") as f:
            for data in close.iter_content(chunk_size=chunk):
                f.write(data)
                cur_size += len(data)
                last = Pro(cur_size,tot_size,start,last)
    print()

def CrawlFile():
    str = input("Please input your url:\n")
    if str=="exit" or str=="q":
        return str
    elif str[0:4] == "http":
        url = str
    else:
        url = "https://" + str
    r = requests.get(url,headers=headers,stream=True)
    if r.status_code == 200:
        filename = url.split('/')[-1]
        if manual or len(filename)>len_limit:
            filename = input("Filename: ")
        path = dir_path+'/'+filename
        size = int(r.headers['content-length'])
        if size>_1MB:
            Download(r,path,size)
        else:
            open(path,'wb').write(r.content)
        if op.isfile(path):
            return "Successful"
        else:
            print("Failed to write into target path.")
            return "Failure"
    else:
        print("status_code == ",r.status_code)
        print("Failed to connect the target url.")
        return "Failure"

def main():
    global manual
    if len(sys.argv)==2 and sys.argv[1]=='-m':
        manual = True
    for i in range(turns):
        result = CrawlFile()
        if result=="exit" or result=="q":
            break
        else:
            print(result)

main()
