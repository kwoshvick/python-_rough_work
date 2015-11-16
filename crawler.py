__author__ = 'kwoshvick'

import urllib.request as rq
from bs4 import BeautifulSoup

url = input('Enter ')


html = rq.urlopen(url).read()
print(type(html))
soup = BeautifulSoup(html)

tags = soup('a')

for tag in tags:
    print(tag.get('href',None))
