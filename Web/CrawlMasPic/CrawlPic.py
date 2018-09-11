#[Standard Tool]
#The programme is to Crawl Pics from a designated website with a url of \
#"url" and save them to a certain existed local dir with the path of    \
#"dir_path"

#coding:utf-8
import requests
import re
import os.path as op
url = 'http://www.ixiumei.com/a/20180702/296918.shtml'
dir_path = '/home/andrew/Downloads/Pic4/'

def SaveFile(url,dir_path):
    r = requests.get(url)
    try:
        with open(dir_path,"wb") as f:
            f.write(r.content)
    except:
        return

def Rename(record,name):
    num = record.count(name)
    if num>0:
        list = name.split('.')
        if len(list)==1:
            name = list[0]+str(num)
        else:
            name = list[0]+str(num)+'.'+list[1]
    return name

def Convert(url,prefix_path):
    r = requests.get(url)
    r.encoding = "utf-8"
    html = r.text
    reg = r'<img (.*?)>'
    img_info = re.findall(reg,html)
    
    num = 0
    suc_num = 0
    list = []
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
        name = Rename(list,pic_name)
        list.append(pic_name)
        dir_path = prefix_path + '/' + name
        try:
            SaveFile(url,dir_path)
            if op.exists(dir_path):
                print(dir_path)
                print("Successful")
                suc_num += 1
            else:
                print("Failed")
        except:
            print("Failed")
    print("Successfully Downloaded %d/%d Pictures into dir_path."%(suc_num,len(img_info)))
        
def main():
    Convert(url,dir_path)

if __name__ == "__main__":
    main()

