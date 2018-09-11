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
    reg = r'<img (.*?)>'
    img_info = re.findall(reg,html)
    
    num = 0
    for i in img_info:
        src_reg = r'src="(.*?)"'
        url = "https:" + re.findall(src_reg,i)[0]
        alt_reg = r'alt="(.*?)"'
        alt = re.findall(alt_reg,i)
        try:
            alt = alt[0]
        except:
            continue
        pic_name = alt + ".jpg"
        path = folder_path + '/' + pic_name
        try:
            print(num)
            SaveFile(url,path)
            num += 1
            print("Successful.")
        except:
            print("Failure.")
            continue
    print("Successfully Downloaded %d/%d Pictures into Path."%(num,len(img_info)))
    
def main():
    url = "https://www.qiushibaike.com/pic/"
    path = '/home/andrew/D/CrawlPic'
    Convert(url,path)
    
if __name__ == "__main__":
    main()


