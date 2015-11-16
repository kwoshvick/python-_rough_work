__author__ = 'kwoshvick'

import urllib.request as rq

fhand = rq.urlopen('http://www.pythonlearn.com/code/intro-short.txt')

for line in fhand:
    print(line.strip())
