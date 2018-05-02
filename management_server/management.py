import os, subprocess, time
import socket
from threading import Thread
# from neutronclient.v2_0 import client as neutronclient
from novaclient.v2.client import client as novaclient
from time import sleep
import openstack_token
from keystoneauth1 import identity
from keystoneauth1 import session
from keystoneauth1.identity import v3
# define some Macros
# cache_num = 4
MAX_SERVERS = 5
MIN_SERVERS = 2
cache_load_data = {}
def receive_from_cache():
    port = 6969
    ip = '0.0.0.0'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip,port))
    while True:

        # print('xyz')
        data, addr = sock.recvfrom(512)
        # print('abc')
        cache_load_data[addr[0]] = float(data.decode("utf-8"))
        # print(data,':',addr)
        print(cache_load_data)
        pass
    pass



# print("efg")
# receive_from_cache(0)
# Defining Macros
LOAD_THRESHOLD = 1000
try:
    OS_token = openstack_token.openstack_token()
except:
    pass
    # print("didnt work brah (OS gettoken())")
NOVA_VERSION = 2
AUTH_URL = 'https://kaizen.massopen.cloud:5000/v3'
SERVICE = 'compute'
PROJECT_NAME = 'BU_CCC18_CDN_and_WAF'
# AUTH_TOKEN = OS_token.get_id()
# print(AUTH_TOKEN)
# if OS_token.check_time():
#     print('Yay!')
#     pass
# I found this python script at the link below
# https://github.com/CCI-MOC/moc-public/wiki/Python-Service-Clients

# There are several ways to set these variables in Python.  In this example, we
# assume you sourced the Openstack RC script and get the correct values from the
# environement. You could also read them into the script from a config file.
# auth_url = os.environ.get('OS_AUTH_URL')
# project_name = os.environ.get('OS_PROJECT_NAME')
# username = os.environ.get('OS_USERNAME')
# password = os.environ.get('OS_PASSWORD')
# region = os.environ.get('OS_REGION_NAME')


######## This is what my environement variables look like
# OS_AUTH_URL=https://kaizen.massopen.cloud:5000/v3
# OS_PROJECT_ID=72e6d9abb926426b8dc64d851df5346c
# OS_PROJECT_NAME=BU_CCC18_CDN_and_WAF
# OS_USER_DOMAIN_NAME=Federated
# OS_PROJECT_DOMAIN_ID=default
# OS_USERNAME=gurber15@bu.edu
# OS_PASSWORD=XXXXXXXXXX
# OS_REGION_NAME=MOC_Kaizen
# OS_INTERFACE=public
# OS_IDENTITY_API_VERSION=3
# OS_PROJECT_DOMAIN_NAME=Default
# OS_AUTH_TYPE=v3oidcpassword
# OS_IDENTITY_PROVIDER=moc
# OS_PROTOCOL=openid
# OS_CLIENT_ID=kaizen-client
# OS_CLIENT_SECRET=fac377a9-f2ba-41e7-bb7f-4064dd9f4468
# OS_ACCESS_TOKEN_ENDPOINT=https://sso.massopen.cloud/auth/realms/moc/protocol/openid-connect/token
# OS_DISCOVERY_ENDPOINT=https://sso.massopen.cloud/auth/realms/moc/.well-known/openid-configuration

# This is the MOC guide I am trying to follow
# https://osticket.massopen.cloud/kb/faq.php?id=16

'''
def get_new_token():
    """Sometime you want to emulate the action of "source" in bash,
    settings some environment variables. Here is a way to do it."""
    env_var = { "OS_AUTH_URL":"https://kaizen.massopen.cloud:5000/v3",
                "OS_USERNAME":"gurber15@bu.edu",
                "OS_PROJECT_NAME":"BU_CCC18_CDN_and_WAF",
                "OS_PROJECT_DOMAIN_NAME":"Default",
                "OS_PASSWORD":"cos55lac", # Read this variable during the start of the script, instead of hard-coding it
                "OS_REGION_NAME":"MOC_Kaizen",
                "OS_AUTH_TYPE":"v3oidcpassword",
                "OS_IDENTITY_PROVIDER":"moc",
                "OS_PROTOCOL":"openid",
                "OS_CLIENT_ID":"kaizen-client",
                "OS_CLIENT_SECRET":"fac377a9-f2ba-41e7-bb7f-4064dd9f4468",
                "OS_ACCESS_TOKEN_ENDPOINT":"https://sso.massopen.cloud/auth/realms/moc/protocol/openid-connect/token",
                "OS_DISCOVERY_ENDPOINT":"https://sso.massopen.cloud/auth/realms/moc/.well-known/openid-configuration",
                "OS_INTERFACE":"public",
                "OS_IDENTITY_API_VERSION":"3"}
    os.environ.update(env_var)
    proc = subprocess.Popen('openstack token issue > token_txt.txt',stdout=subprocess.PIPE,shell=True)
    pass
    '''
# def shell_source():
#

# while True:
#     #     # if token about to expire or is None,
#     #     get new token
#     #     connection = new connection using new token
#     # balance_load(connection)
#     sleep(20)
#     password
nova = novaclient.Client(version = 2, auth_token=OS_token.get_id(),
                         auth_url = AUTH_URL,
                         service_type=SERVICE,
                         project_name= PROJECT_NAME,
                         project_domain_name='Default')

def increment_server(server_name = "VarnishCache4"):
    print("Incrementing Server")
    # nova = novaclient.Client(version = 2, auth_token=OS_token.get_id(),
    #                          auth_url = AUTH_URL,
    #                          service_type=SERVICE,
    #                          project_name= PROJECT_NAME,
    #                          project_domain_name='Default')
    # server_name = server_name_given + str(cache_num)
    # cache_num = cache_num + 1
    block_mapping = [{"source_type": "snapshot", "delete_on_termination": True, "boot_index": 0,
                        "uuid": "dfbbc241-b8fc-4bcd-9ab7-96caa7abe71b", "destination_type": "volume"}]
    newServer=(nova.servers.create(flavor='480b1763-ec02-485c-b39a-78e3d9d8c167',image=None, name=server_name,block_device_mapping_v2=block_mapping))
    # newServer.add_floating_ip("128.31.25.73")
    time.sleep(50)
    return newServer

    pass


# load_value = 1500
def load_scale():
    # get load status on all caching servers
    while True:
        pass
        load = 0

        while not cache_load_data:
            pass
        for key,value in cache_load_data.items():
            load = load + (value)
            pass
            # print("value = ",value)
        load = load/len(cache_load_data)
        #     # if load > threshold:
        # print("Load = ",load)
        if (load > LOAD_THRESHOLD) and (len(cache_load_data)< MAX_SERVERS):
    #         # start new instance

            print("Load is higher than threshold")
            increment_server()
            # increment_server().networks['CDN_internal'][0] #-> this is the local ip of the new server.
            # add new server ip to dns and  customer list
            # break
            pass
        else:
            if (load < LOAD_THRESHOLD) and (len(cache_load_data) > MIN_SERVERS):
                # delete one instance
                    pass
        #     start new instances
        # else:
        #     if number of instances > default number:
        #         reduce number of instances
        time.sleep(10)
        pass
# AUTH_TOKEN = 'gAAAAABa3RWo4BtVCOCeXFicJTrPdKLwjzf4k8EXmEQ8V-1Sy_scZ5ROZ0XcS5qNjmvdlsrijIWzuRsDQreiXbhMBzApLxj81nVCsLQiWm2qUUWThVpkqAVuEz5lDxWBArm-nA4Oip3uhCp5BwjN-1MUQiT8j-OKhyZAD_xZpVR55i5vAAkzSOeuRzlaFFVDEP5av7QQG8G8'
# get_new_token()
# nova = novaclient.Client(version = 2, auth_token=OS_token.get_id(),
#                          auth_url = AUTH_URL,
#                          service_type=SERVICE,
#                          project_name= PROJECT_NAME,
#                          project_domain_name='Default')
# neutron = neutronclient.Client(auth_token=OS_token.get_id(),
#                          auth_url = AUTH_URL,
#                          service_type='network',
#                          project_name= PROJECT_NAME,
#                          project_domain_name='Default')
# sess = session.Session(auth=auth)
# neutron = client.Client(session=sess)
# env_var = { "auth_url":"https://kaizen.massopen.cloud:5000/v3",
#             "username":"gurber15@bu.edu",
#             "project_name":"BU_CCC18_CDN_and_WAF",
#             "project_domain_name":"Default",
#             "password":'cos55lac', # Read this variable during the start of the script, instead of hard-coding it
#             "region_name":"MOC_Kaizen",
#             "auth_type":"v3oidcpassword",
#             "identity_provider":"moc",
#             "protocol":"openid",
#             "client_id":"kaizen-client",
#             "client_secret":"fac377a9-f2ba-41e7-bb7f-4064dd9f4468",
#             "access_token_endpoint":"https://sso.massopen.cloud/auth/realms/moc/protocol/openid-connect/token",
#             "discovery_endpoint":"https://sso.massopen.cloud/auth/realms/moc/.well-known/openid-configuration",
#             "interface":"public",
#             "identity_api_version":"3"}
# floating_ip = nova.floating_ip_pools.list()
# print(ipClient(**env_var, version=nova).floating_ip_pools.list())
# print(nova.volumes.get_server_volumes())
# get list of all customers (emails) Here customer_list = []
# get list of all server names
# somehow distribute servers to customers
# then balance load
# block_mapping = {'dfbbc241-b8fc-4bcd-9ab7-96caa7abe71b':'volume'}
# block_mapping = [{"source_type": "snapshot", "delete_on_termination": True, "boot_index": 0, "uuid": "dfbbc241-b8fc-4bcd-9ab7-96caa7abe71b", "destination_type": "volume"}]
# for x in (nova.flavors.list()):
#     print (x, ':', x.id)
# print(nova.servers.create(flavor='480b1763-ec02-485c-b39a-78e3d9d8c167',image=None, name='VarnishCache5',block_device_mapping_v2=block_mapping))
# neutron = neutronclient.Client(auth_token=OS_token.get_id(),
#                          auth_url = AUTH_URL,
#                          service_type='network',
#                          project_name= PROJECT_NAME,
#                          project_domain_name='Default',
#                          endpoint_url='https://kaizen.massopen.cloud:9696/')
# print(neutron.list_floatingips())
# for server in nova.servers.list():
#     if server.name == 'VarnishCache5':
#         server.delete()
#         pass
# #     print(nova.volumes.get_server_volumes(server_id = server.id)[0].id)
#     print(server.interface_list(), ' : ',server.networks['CDN_internal'][0])
#     pass
# instances = nova.servers.get('acd9d1c1-81e8-4e23-bcb6-bbae89d7a152')
# STATUS = instances.status
# print (STATUS)
# instances.start()
# # print (instances.status)
#
# # while ( STATUS == 'SHUTOFF'):
#     # print (instances.status)
#     # sleep(2)
#     # STATUS = instances.status
#     # pass
# # instances.stop()
# print (instances.status)
# print(nova.servers.list())
# increment_server()
# This is the response I get when I try to run this script with the correct password.
# keystoneauth1.exceptions.http.Unauthorized: The request you have made requires authentication. (HTTP 401) (Request-ID: req-b4839f94-9556-478b-b41e-febe14333741)
# Thanks for helping

thread = Thread(target = receive_from_cache)

thread2 = Thread(target = load_scale)
thread.start()
thread2.start()
# thread.start_new_thread(receive_from_cache,())
# thread.start_new_thread(load_scale,())
