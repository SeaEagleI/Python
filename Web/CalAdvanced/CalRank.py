#coding:utf-8
import requests
from bs4 import BeautifulSoup
import bs4

#url = "http://www.gaosan.com/gaokao/184263.html"
url = "http://www.cse.neu.edu.cn/SinglePage.aspx?news_id=b3d56656-e43c-4d1c-b8fe-61d97eb1679c&navigation_id=%u9996%u9875&module=%u901A%u77E5%u516C%u544A&cat=1"
lines = 50

def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
    pass

def printUnivList(ulist,num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
    pass
    
def main():
    uinfo = []
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,lines)
    pass
    
    
if __name__ == "__main__":
    main()






















