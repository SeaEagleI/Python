#coding:utf-8
import requests
import re
import os.path as op
import os

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
    reg = r'<img (.*?)>'
    img_info = re.findall(reg,html)
    
    num = 0
    suc_num = 0
    list = []
    for i in img_info:
        num += 1
        print(num)
        
        src_reg = r'src="(.*?)"'
        url = "https:" + re.findall(src_reg,i)[0]
        alt_reg = r'alt="(.*?)"'
        alt = re.findall(alt_reg,i)
        try:
            alt = alt[0]
        except:
            print("Failed")
            continue
        if alt == "":
            print("Failed")
            continue
        if list.count(alt) == 0:
            list.append(alt)
        else:
            print("Skipped")
            continue
        
        pic_name = alt + ".jpg"
        print(pic_name)
        path = folder_path + '/' + pic_name
        try:
            SaveFile(url,path)
            if op.exists(path):
                print("Successful")
                suc_num += 1
            else:
                print("Failed")
        except:
            print("Failed")
    print("Successfully Downloaded %d/%d Pictures into Path."%(suc_num,len(img_info)))
    
def main():
    url = "https://www.qiushibaike.com/pic/"
    #path = "/home/andrew/D/Crawl/CrawlPic2"
    print("Please input path of your Save_Folder:(ABS path without '/' in the end)")
    print("Examples: /home/andrew/D/CrawlPic")
    path = input("")
    if op.exists(path) == False:
        os.makedirs(path)
    Convert(url,path)
    
if __name__ == "__main__":
    main()
