#!/usr/bin/env python3
# Management server will get the data using the following commands
# need to add this to the main file
import socket, time
from load_tester import *

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP connection to the management server

MANAGEMENT_IP = '155.41.60.148' # Change this to a non static url
MANAGEMENT_PORT = 6969

while True: # need to figure out how to run this in a new thread or process
    data = (str(get_average(5))).encode()
    # print(data)
    sock.sendto(data,(MANAGEMENT_IP,MANAGEMENT_PORT))
    time.sleep(1)
    pass
