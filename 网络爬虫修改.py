#e23.1CrawUnivRanking.py
import requests
from bs4 import BeautifulSoup
allUniv = []
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
def fillUnivList(soup):
    data = soup.find_all('tr')
    for tr in data:
        ltd = tr.find_all('td')
        if len(ltd)==0:
            continue
        singleUniv = []
        for td in ltd:
            singleUniv.append(td.string)
        allUniv.append(singleUniv)
def printUnivList(num):
    print("{:^4}{:^20}{:^5}".format("排名","学校名称","总分"))
    for i in range(num):
        u=allUniv[i]
        print("{:^4}{:^20}{:^5}.format(u[0],u[1],u[2]))
def main():
    url = 'http://www.zuihaodaxue.cn/Sport-Science-Schools-and-Departments-2017.html'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")
    fillUnivList(soup)
    printUnivList(10)
main()
