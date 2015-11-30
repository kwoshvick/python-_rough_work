__author__ = 'kwoshvick'

import urllib.request as rq
import json
list_numbers = list()


# http://python-data.dr-chuck.net/comments_42.json
# http://python-data.dr-chuck.net/comments_171968.json


url = input("Please Enter URL: ")
urlhandler = rq.urlopen(url).read().decode()
jsondata = json.loads(urlhandler)
#print(json.dumps(jsondata,indent=4))
comments = jsondata['comments']
#print(comments)
for numbers in comments:
    num=int(numbers['count'])
    list_numbers.append(num)

print(sum(list_numbers))





