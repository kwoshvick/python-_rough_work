__author__ = 'kwoshvick'

#python 3

import urllib.request as rq
from bs4 import BeautifulSoup


url = input('Enter ')
numbers = list()


html = rq.urlopen(url).read()

soup = BeautifulSoup(html)

tags = soup('span')

for tag in tags:
    numbers.append(int(tag.string))

print(sum(numbers))
