#coding:utf-8
import xlrd

path = "/home/andrew/Python/Web/CalAdvanced/dict.xls"
dict = {}

wb = xlrd.open_workbook(path)
sheet = wb.sheets()[0]
for i in range(sheet.ncols):
    values = sheet.col_values(i)
    head = values[0]
    rows = len(values)
    for j in range(1,rows):
        dict[head] = values[j]
print(dict) 


















