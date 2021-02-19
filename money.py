from urllib import request,parse
import json
import time
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
number=0
caesar=0
def comment(id,re):
    url = 'https://api.bilibili.com/x/web-interface/coin/add'
    header = {'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:85.0) Gecko/20100101 Firefox/85.0",
              'cookie': "",
              'referer':re
    }
    data = {
            'aid':id,
            'multiply': '1',
            'select_like': "0",
            'cross_domain': 'true',
            'csrf': 'e631c26d38044b51b0a311883355eeb8' #没有过多研究，个人理解为每个用户拥有的验证特征码  需要自行去手动评论F12抓包获取
        }
    data=parse.urlencode(data).encode('utf-8')
    html=request.Request(url=url, headers=header,data=data,method='POST')
    print(html)
    response = request.urlopen(html)
    data = response.read()
    data=json.loads(data)
    print(data)
def video():
    global number,ref
    url="https://api.bilibili.com/x/web-interface/search/type?context=&page=1&order=pubdate&keyword=%E5%85%89%E9%81%87&duration=0&tids_2=&__refresh__=true&_extra=&search_type=video&tids=0&highlight=1&single_column=0"
    header={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11.1; rv:85.0) Gecko/20100101 Firefox/85.0"}
    html=request.Request(url,headers=header)

    req=request.urlopen(html)

    if req.getcode()==200:
        r=req.read()
        r=json.loads(r)
        r=r["data"]["result"][0]
        number=r["id"]
        ref=r["arcurl"]

video()

num=number
b=0

while True:
    caesar=caesar+1
    if caesar==15:
        video()
        numm=number
        if num!=numm:
            b=b+1
            num=numm
            comment(number,ref)
            print("你币没了"+str(b)+"个")
        caesar=0
        if b==10:
            break
    time.sleep(1)

