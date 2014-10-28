import requests
import json 
from BeautifulSoup import BeautifulSoup




url = 'http://www.krx.co.kr/por_kor/popup/JHPKOR13008.jsp'
r = requests.post(url, data={'mkt_typ':'S', 'market_gubun': 'allVal'})


soup = BeautifulSoup(r.text)
table = soup.find('table', {'id':'tbl1'})
trs = table.findAll('tr')

stock_list = []

for tr in trs[1:5]:
    stock = {}
    cols = tr.findAll('td')
    stock['code'] = cols[0].text[1:]
    stock['name'] = cols[1].text[1:]
    stock['full_code'] = cols[2].text
    stock_list.append(stock)


print stock_list




