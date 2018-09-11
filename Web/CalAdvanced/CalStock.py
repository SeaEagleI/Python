#coding:utf-8
import requests
import re
import time
#import traceback
import os.path as op
from math import ceil
from bs4 import BeautifulSoup
start = time.perf_counter()
start_num = 200
CrawlNum = 100

def Pro(num,total,scale=50):
    count = ceil((num/total)*scale)
    a = '*' * count
    b = '.' * (scale-count)
    c = (num/total)*100
    dur = time.perf_counter() - start
    if count<= total-2:
        print("\r{:^5.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
    else:
        print("\r{:^5.0f}%[{}{}]{:.2f}s".format(c,a+'*'*2,b,dur),end="")

def getHTMLText(url,code='utf-8'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return None
    
def getStockList(lst,stockURL):
    html = getHTMLText(stockURL,'GB2312')
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}',href)[0])
        except:
            continue

def getStockInfo(lst,stockURL,fpath):
    count = 0
    end_num = start_num + CrawlNum + 1
    for i in range(start_num,end_num):
        stock = lst[i]
        url = stockURL + stock + '.html'
        html = getHTMLText(url)
        try:
            if html=="":
                continue
            infoDict = {}
            soup = BeautifulSoup(html,'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})
            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})
            
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
                
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                if count>=CrawlNum:
                    break
                Pro(count,CrawlNum)
            
        except:
            count = count + 1
            if count>=CrawlNum:
                break
            Pro(count,CrawlNum)
            continue
            
def main():
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    path = "/home/andrew/Python/Web/CalAdvanced/StockInfo"
    slist = []
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,path)
    if op.isfile(path):
        print("\nSuccessful")
    else:
        print("\nFailure")
            
main()
