#encoding:utf-8
import requests
import json

url = 'http://fanyi.baidu.com/basetrans'
headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS \
            9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, \
            like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'} 


word = 'archaeologists'
data = {'query':word,'from':'en','to':'zh'}
r = requests.post(url, headers=headers, data=data)
code = r.content.decode()
result = json.loads(code)['trans'][0]['dst']



