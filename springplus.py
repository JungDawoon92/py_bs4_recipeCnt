import requests
from bs4 import BeautifulSoup
import re

for i in range(1, 5):
    req = requests.get('https://www.hansik.or.kr/kr/board/re/list/323?seq=&bbsId=323&curPage=' + str(
        i) + '&bbsType=re&menuId=193&searchWord=&rowSize=50')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    cooktitle = soup.findAll('td', {"class": "recipe-title"})

    for div in cooktitle:

        subject = div.text
        subject = subject + '만들기'
        print(subject)

        url = 'https://www.youtube.com/results?search_query=' + subject + '&sp=CAMSBAgFEAE%253D'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

        req = requests.get(url, headers=headers)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        review = soup.find_all(string=re.compile('조회수 '))

        asdf = str(review)

        st = [m.end() for m in re.finditer('조회수 ', asdf)]
        ed = [m.start() for m in re.finditer('회"}', asdf)]

        try:
            qwe = asdf[st[1]:ed[1]]
            replaceAll = qwe.replace(",", "")
            finalcount = int(replaceAll)
        except Exception as ex:
            replaceAll = 0
            finalcount = int(replaceAll)

        print(finalcount)