#!/usr/bin/env python3

from urllib.parse import urlparse
from urllib.parse import urlsplit

# import urllib
# import socket
# print(socket.gethostbyname('google.com'))

# o = urlsplit('www.google.com/home/bevf/dvfv')

# p = urlsplit('google.com')
myWebList = ['http://google.co.in/home/bevf/dvfv','google.com', 'docs.google.com', 'google.co.in']

# for url in myWebList:
#     # print(i.split("//")[-1].split("/")[0].split('?')[0])
#     spltAr = url.split("://");
#     i = (0,1)[len(spltAr)>1];
#     dm = spltAr[i].split("?")[0].split('/')[0].split(':')[0].lower();
#     print(dm)
o = urlparse(myWebList[0])
print(o.hostname)
print(o)
