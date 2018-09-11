#coding:utf-8
import requests
import re

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
    html = r.text
    reg = r'<img src="(.*?)"'
    img_urls = re.findall(reg,html)
    
    num = 0
    for i in img_urls:
        pic_name = i.split("/")[-1]
        path = folder_path + '/' + pic_name
        try:
            SaveFile(i,path)
            ++num
            print("Successful.")
        except:
            print("Failure.")
            continue
    print("Successfully Downloaded %d Pictures into Path."%(num))
    
def main():
    url = "https://www.qiushibaike.com/pic/"
    path = '/home/andrew/D/CrawlPic'
    Convert(url,path)
    
if __name__ == "__main__":
    main()


