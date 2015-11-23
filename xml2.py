__author__ = 'kwoshvick'
'''
url to fetch
http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.xml

http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_171964.xml
'''


import urllib.request as rq
import xml.etree.ElementTree as ET


url = input('Enter ')
numbers = list()


xml = rq.urlopen(url).read()
tree = ET.fromstring(xml)

lst = tree.findall('comments/comment')

for item in lst:
    n = item.find('count').text
    numbers.append(int(n))

print(sum(numbers))

