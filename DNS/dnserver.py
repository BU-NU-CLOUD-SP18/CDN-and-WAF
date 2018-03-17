#!/usr/bin/env python3

import socket
from dnslib import *

port = 53
ip = '127.0.0.1'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip,port))

while 1:
    data, addr = sock.recvfrom(512)
    print(data)
    question = DNSRecord.parse(data)
    print(question)
    answer = question.reply()
    answer.add_answer(*RR.fromZone("abc.com 60 CNAME www.google.com"))
    # print(answer)
    sock.sendto(answer.pack(), addr)
