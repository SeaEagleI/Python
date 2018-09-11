#coding:utf-8
import xlwt
import os.path as op

head = ['Name',"Age"]
dict = {'Name':"WDJ",'Age':"19"}
path = "/home/andrew/Python/Web/CalAdvanced/dict.xls"

#Create worksheet
wb = xlwt.Workbook(encoding='utf-8')
sheet = wb.add_sheet('sheet1')

#headings
for i in range(2):
    sheet.write(0,i,label=head[i])


for key,val in dict.items():
    if key==head[0]:
        sheet.write(1,0,val)
    elif key==head[1]:
        sheet.write(1,1,val)
    else:
        continue

#Save xls
wb.save(path)
if op.isfile(path):
    print("Successful")
