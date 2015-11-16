__author__ = 'kwoshvick'

'''
First test link -> http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html
answer --> http://pr4e.dr-chuck.com/ ... /known_by_Anayah.html

Second Test link -> http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Ayyub.html
answer --> http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Seo.html
'''



import urllib.request as rq
from bs4 import BeautifulSoup

url = input('Enter link ')
count = input('Enter Position ')
repeat = input('Enter repeat ')

urllist = list()
last_link = list()

def go_to_url(link):
    global soup
    global tags
    html = rq.urlopen(link).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    return tags

def iterate_links(link , count):
    tags = go_to_url(link)
    counter = 0
    for tag in tags:
        if counter <= (count-1):
            urllist.append(tag.get('href'))
            counter += 1
        else:
            break

    return urllist[-1]


def get_last_link(link,count,repeat):
    new_link = iterate_links(link,count)
    no_iterations = 1
    while no_iterations <= repeat:
        last_link.append(new_link)
        new_link = iterate_links(new_link,count)
        no_iterations +=1




get_last_link(url,int(count),int(repeat))

#print(len(urllist))
print(last_link[-1])


