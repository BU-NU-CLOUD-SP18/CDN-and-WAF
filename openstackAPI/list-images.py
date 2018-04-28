import os
import json
import pprint
from openstack import connection
from openstack import profile


# There are several ways to set these variables in Python.  In this example, we
# assume you sourced the Openstack RC script and get the correct values from the
# environement. You could also read them into the script from a config file.
# auth_url = os.environ.get('OS_AUTH_URL')
# project_name = os.environ.get('OS_PROJECT_NAME')
# username = os.environ.get('OS_USERNAME')
# password = os.environ.get('OS_PASSWORD')
# region = os.environ.get('OS_REGION_NAME')

auth_url = "https://kaizen.massopen.cloud:5000/v3"
project_name = "BU_CCC18_CDN_and_WAF"
username = "asan@bu.edu"
password = "doNOTuseMYaccount"
region = "MOC_Kaizen"

def create_connection(auth_url,region,project_name,username,password):
    """ Connect and authenticate to OpenStack

    This function came straight from the Openstack docs:
    http://developer.openstack.org/sdks/python/openstacksdk/users/guides/connect.html
    """
    prof = profile.Profile()
    prof.set_region(profile.Profile.ALL, region)
    return connection.Connection(
        profile=prof,
        user_agent="kaizen-client",
        auth_url=auth_url,
        project_name=project_name,
        username=username,
        password=password)

def readable_format(img):
    img_dict = img.to_dict()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(img_dict)


# connect & authenticate
conn = create_connection(auth_url,region,project_name,username,password)

# print name and ID of all available images
for image in conn.compute.images():
     print("{ID}\t{name}".format(ID=image.id, name=image.name))


# print all data about the first image in the list
image1 = conn.compute.images().next()
print(image1)


# Uncomment the function below to print the image info in an easy to read format
#readable_format(image1)
