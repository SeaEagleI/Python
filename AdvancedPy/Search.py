#coding:utf-8
import requests
import re
import time

prefix_url = "http://dict.youdao.com/search?q="
suffix_url = "&keyfrom=dict.index"
hint = "Crawling interpretation results from YoudaoTrans,\
      \nwe are now trying best to serve you with extreme experiences.\
      \nIf you'd like to exit, press 'q'.\
      \nOtherwise,you'll enter into a circulation of translation.\
      \nNow,just enjoy it! (English -> Chinese)\
      \nRemember:Input A single word at a time."
turns = 100

def search(word):
    url = prefix_url+word+suffix_url
    r = requests.get(url)
    r.encoding = 'utf-8'
    html = r.text
    result = re.search(r"(?s)<div class=\"trans-container\">\s*<ul>.*?</div>",html)
    try:
        means = re.findall(r"(?m)<li>(.*?)</li>",result.group())
        return means
    except:
        return None
    pass

def main():
    print(hint+'\n')
    for i in range(turns):
        word = input("Input ["+str(i+1)+"]:")
        #start = time.perf_counter()
        if word=="q":
            break
        else:
            list = search(word)
            print("Result["+str(i+1)+"]:")
            for item in list:
                print("{}".format(item))
            #print("(Time used in {:^.4}s)".format(time.perf_counter()-start))
            print("")

if __name__ == "__main__":
    main()
