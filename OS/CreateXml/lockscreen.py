#coding:utf-8
import os.path as op
import os

pic_path = "/home/andrew/Pictures/"
bg_path = "/usr/share/backgrounds/"
xml_path = "/usr/share/backgrounds/contest/lockscreen.xml"
head = "<background>\n  <starttime>\n    <year>2018</year>\n    <month>09</month>\n\
    <day>09</day>\n    <hour>15</hour>\n    <minute>02</minute>\n\
    <second>00</second>\n  </starttime>\n<!-- Animation start time: 2018-09-09 15:02:00. -->\n"
tail = "</background>"

last_time = 2     #minutes
trans_time = 0.5     #seconds

def getString(pic1,pic2):
    string = ""
    line = ['' for i in range(9)]
    static_time = last_time*60-trans_time
    
    line[0] = '  <static>'
    line[1] = '    <duration>' + str(static_time) + '</duration>'
    line[2] = '    <file>' + pic_path + pic1 + '</file>'
    line[3] = '  </static>'
    line[4] = '  <transition>'
    line[5] = '    <duration>'+str(trans_time)+'</duration>'
    line[6] = '    <from>' + pic_path + pic1 + '</from>'
    line[7] = '    <to>' + pic_path + pic2 + '</to>'
    line[8] = '  </transition>'
    for items in line:
        string = string+items+'\n'
    return string

def getText():
    txt = ""
    list = os.listdir(pic_path)
    for i in list:
        if i.find('.jpg')==-1:
            list.remove(i)
    num = len(list)
    for i in range(len(list)):
        if i!=num-1:
            txt += getString(list[i],list[i+1])
        else:
            txt += getString(list[i],list[0])
    txt = head+txt+tail
    return txt

def WriteXml(string,path=xml_path):
    f = open(path,'w')
    f.write(string)
    f.close()
    if op.isfile(path):
        print("Successfully Created Lock Screen")
    else:
        print("Failure to Create Lock Screen")

def main():
    txt = getText()
    WriteXml(txt)
    
main()

