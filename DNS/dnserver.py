#!/usr/bin/env python3

import socket
from dnslib import *

port = 53
ip = '127.0.0.1'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip,port))

while 1:
    data, addr = sock.recvfrom(512)
    # print("This is data:")
    # print(data)
    question = DNSRecord.parse(data)
    parsedQ = question.get_q()
    print("This is the Parsed Question")
    print(question)
    answer = question.reply()
    answer.add_answer(*RR.fromZone(str(parsedQ.get_qname())+" 299 A 172.217.12.196"))
    # print("This is the response packet")
    # print(answer)
    sock.sendto(answer.pack(), addr)
