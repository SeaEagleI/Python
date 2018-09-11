#coding:utf-8
import requests
import os.path as op
import os

url = "http://img1.mm131.me/pic/2330/"
path = "/home/andrew/D/Crawl/CrawlPic3"

def SaveFile(url,path):
    r = requests.get(url)
    try:
        with open(path,"wb") as f:
            f.write(r.content)
    except:
        return

def Convert(url,folder_path):
    r = requests.get(url)
    r.encoding = "utf-8"
    for i in range(30,51):
        url = url + str(i) + ".jpg"
        pic_name = str(i) + ".jpg"
        path = folder_path + '/' + pic_name
        SaveFile(url,path)
    
def main():
    if op.exists(path) == False:
        os.makedirs(path)
    Convert(url,path)
    
if __name__ == "__main__":
    main()
