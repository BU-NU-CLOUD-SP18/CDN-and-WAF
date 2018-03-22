#!/usr/bin/env python3

import socket
from dnslib import *
from urllib.parse import urlparse

def queryExternalDNS(data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    sock.sendto(data,("8.8.8.8",53))
    recvData, addr2 = sock.recvfrom(1024)
    return recvData
port = 53
ip = '0.0.0.0'
customerID = 'abc@bu.edu'
customerDomains = ['4n4nd.me', 'www.4n4nd.me']

cacheServerIPs = ["128.31.26.6","128.31.25.244","128.31.26.50"]
roundrobinINT = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip,port))
# socket2.sendto
while 1:
    data, addr = sock.recvfrom(512)
    query = DNSRecord.parse(data)
    domain = str(DNSRecord.parse(data).get_q()).split()[0][1:][:-1]
    # print(str(DNSRecord.parse(data).get_q()).split()[0][1:][:-1])
    if domain not in customerDomains:
        sock.sendto(queryExternalDNS(data),addr)
    else:
        # print("This is data:")
        # print(data)
        # send query to google's DNS server


        # question = DNSRecord.parse(data)
        # parsedQ = question.get_q()
        # print("This is the Parsed Question")
        # print(question)
        returnIP = cacheServerIPs[roundrobinINT]
        roundrobinINT += 1
        if roundrobinINT >= len(cacheServerIPs):
            roundrobinINT = 0
        response = query.reply()
        response.add_answer(*RR.fromZone(domain+" 299 A "+returnIP))
        print("This is the response packet")
        print(response)

        # sock.sendto(answer.pack(), addr)
        sock.sendto(response.pack(),addr)
