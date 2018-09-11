#coding:utf-8
from selenium import webdriver
url = "https://www.douban.com/"
tel = "574609917@qq.com"
word = "wdj1234567"

name_xpath = '''//*[@id="form_email"]'''
passwd_xpath = '''//*[@id="form_password"]'''
click_xpath = '''//*[@id="form_remember"]'''
submit_xpath = '''/html/body/div[2]/div/div[1]/form/fieldset/div[3]/input'''


browser = webdriver.Firefox()
p = browser.get(url)

browser.find_element_by_xpath(name_xpath).clear()
browser.find_element_by_xpath(name_xpath).send_keys(tel)
browser.find_element_by_xpath(passwd_xpath).clear()
browser.find_element_by_xpath(passwd_xpath).send_keys(word)
browser.find_element_by_xpath(name_xpath).click()
browser.find_element_by_xpath(submit_xpath).click()










