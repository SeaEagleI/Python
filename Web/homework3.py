#coding:utf-8
import requests
import re
import os.path as op

url = "http://tieba.baidu.com/p/2937218556"
path = '/home/andrew/D/CrawlPic1'


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
    for i in img_info:
        src_reg = r'src="(.*?)"'
        num += 1
        print(num)
        try:
            url = re.findall(src_reg,i)[0]
        except:
            print("Failed")
            continue
        pic_name = url.split("/")[-1]
        path = folder_path + '/' + pic_name
        try:
            SaveFile(url,path)
            if op.isfile(path):
                print("Successful")
                suc_num += 1
            else:
                print("Failed")
        except:
            print("Failed")
    print("Successfully Downloaded %d/%d Pictures into Path."%(suc_num,len(img_info)))
        
    
def main():
    Convert(url,path)
    
if __name__ == "__main__":
    main()


