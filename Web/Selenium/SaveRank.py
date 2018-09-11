#coding:utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import os.path as op
import xlwt,time
import bs4

url = "http://www.cse.neu.edu.cn/SinglePage.aspx?news_id=b3d56656-e43c-4d1c-b8fe-61d97eb1679c&navigation_id=%u9996%u9875&module=%u901A%u77E5%u516C%u544A&cat=1"
xls_path = "/home/andrew/Desktop/Python/Web/Selenium/GPA-Rankings.xls"
lines = 50
cols = 3

def getHtml(driver,url):
    driver.get(url)
    html = driver.execute_script("return document.documentElement.outerHTML")
    return html

def getList(html):
    list = []
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            list.append([tds[0].string,tds[1].string,tds[2].string])
    for i in range(len(list)):
        for j in range(len(list[i])):
            for ch in "\n\t ":
                list[i][j] = list[i][j].replace(ch,'')
    return list

def WriteXls(list):
    head = []
    for item in list[0]:
        head.append(item)
    ncols = len(head)
    nrows = len(list)
    wb = xlwt.Workbook(encoding='utf-8')
    sheet = wb.add_sheet('sheet1')
    for i in range(ncols):
        sheet.write(0,i,label=head[i])
    for i in range(1,nrows):
        for j in range(ncols):
            sheet.write(i,j,list[i][j])
    wb.save(xls_path)
    if op.isfile(xls_path):
        print("Successfully Saved to Xls")

def main():
    driver = webdriver.Firefox()
    html = getHtml(driver,url)
    list = getList(html)
    WriteXls(list)

main()





