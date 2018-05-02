#!/usr/bin/env python3

import socket
port = 6969
ip = '0.0.0.0'

while 1:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip,port))
    data, addr = sock.recvfrom(512)
    print(data,':',addr)
    pass
