__author__ = 'kwoshvick'

import socket as socks

mySocks = socks.socket(socks.AF_INET , socks.SOCK_STREAM)

mySocks.connect(('www.py4inf.com', 80))

mySocks.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n'.encode('ascii') )

while True:
    data = mySocks.recv(512)
    if (len(data) < 1):
        break
    print(data)
    print()
mySocks.close()
