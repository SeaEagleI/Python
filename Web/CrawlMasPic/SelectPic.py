#Aim:
#The programme is to select and rename certain pics which sizes are \
#over a threshold of "threshold_size kb" from a designated          \
# dir with path "dir_path".                                           \
#And the new Picname is according to a countable order from a start \
#number called "rename_start".

#coding:utf-8
import os
import os.path as op
#from PIL import Image
dir_path = '/home/andrew/Pictures'
threshold_size = 300
rename_start = 0

def pro(size):
    bytes = float(size)
    if bytes>=1024:
        kb = bytes/1024
    else:
        size_str = str(bytes)+'B'
        return size_str
    if kb>=1024:
        mb = kb/1024
    else:
        size_str = str(kb)+'kb'
        return size_str
    size_str = str(mb)+'mb'
    return size_str

def pro_kb(size):
    bytes = float(size)
    return bytes/1024

def main():
    num = rename_start
    dirlist = os.listdir(dir_path)
    for i in dirlist:
        path = dir_path + '/' + i
        if op.isfile(path)==False:
            continue
        sz = op.getsize(path)
        kb = pro_kb(sz)
        if kb>threshold_size:
            num = num+1
            list = i.split('.')
            filename = str(num)+'.'+list[1]
            dest = dir_path+'/'+filename
            os.rename(path,dest)
            print(i)
            print('[{}]:\n{:.1f}kb'.format(num,kb))
            print()

if __name__ == "__main__":
    main()


