import requests
from bs4 import BeautifulSoup
import re

def getHTMLText(url,coding='gbk'):
    try:
        r = requests.get(url,timeout=30)
        print(r)
        r.raise_for_status()
        r.encoding = coding
        return r.text
    except:
        return ""


def downloadImageFile(imgUrl, destUrl, fname=''):
    local_filename = imgUrl.split('/')[-1]
    print('Download Image File={}'.format(local_filename))
    try:
        r = requests.get(imgUrl, stream=True)
        r.raise_for_status()

        if len(fname) == 0:
            fname = local_filename
        print('fname={}'.format(fname))
        with open(destUrl + "/" + fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
            f.close()
        return r.status_code
    except:
        return r.status_code
def getImg(html):
    imgre = re.compile('"objURL":"(.*?)"')
    imglist = re.findall(imgre,html)
    return imglist

def download(urls,path):
    index = 1
    for url in urls:
        print("Download Image from page:{}".format(url))
        status = downloadImageFile(url,path,str(index)+".jpg")
        try:
            if str(status)[0] == '4':
                print("未下载成功{}".format(url))
                continue
        except Exception as e:
            print("未下载成功{}".format(url))
        index += 1

page = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E8%BF%AA%E4%B8%BD%E7%83%AD%E5%B7%B4'
html= getHTMLText(page,'utf-8')
download(getImg(html),'e:\\1149674601')

