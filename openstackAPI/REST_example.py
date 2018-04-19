import argparse
import json
import os
from keystoneauth1.identity import v2, v3
from keystoneauth1 import session


if __name__ == "__main__":

    # Code block below sets up--v2 and --v3 arguments to this script.
    parser = argparse.ArgumentParser(description='Specify v2 or v3 auth')
    version = parser.add_mutually_exclusive_group(required=True)
    version.add_argument('--v2', action='store_true',
                         help='use Keystone auth v2')
    version.add_argument('--v3', action='store_true',
                         help='use Keystone auth v3')
    args = parser.parse_args()

    # In this example, we assume you sourced the Openstack RC script and
    # read these values from the environement.
    auth_url = "https://kaizen.massopen.cloud:5000/v3"
    project_name = "BU_CCC18_CDN_and_WAF"
    user_name = "asan@bu.edu"
    project_id = "72e6d9abb926426b8dc64d851df5346c"
    password = "doNOTuseMYaccount"
    region = "MOC_Kaizen"
    # Note that the environment variable OS_AUTH_URL set in the currrently
    # available RC scripts specifies v2.0. Here we split off the version
    # so that in this script we can choose v2 or v3.
    keystone_base = auth_url.rsplit('/', 1)[0]

    if args.v2:
        auth = v2.Password(auth_url='{}/v2.0'.format(keystone_base),
                           tenant_name=project_name,
                           username=user_name,
                           password=password)

    elif args.v3:
        auth = v3.Password(auth_url='{}/v3'.format(keystone_base),
                           project_name=project_name,
                           project_domain_id='default',
                           username=user_name,
                           user_domain_id='default',
                           password=password)

    # Establish an authenticated session
    sess = session.Session(auth=auth)

    # A full list of available public API endpoints is at:
    #     Compute --> Access & Security --> API Access
    # Some will need to include your project ID, some will not
    nova_url = 'https://nova.kaizen.massopencloud.org:8774/v2/{}'.format(project_id)
    glance_url = 'https://glance.kaizen.massopencloud.org:9292'

    # Here we retrieve a list of available images
    # Since the glance endpoint does not include a version, we discover
    # the current version
    # More information about service discovery can be found here:
    # https://docs.openstack.org/developer/keystoneauth/using-sessions.html#service-discovery
    # Note that the below discovery does not work for
    response = sess.get(glance_url)
    glance_versions = json.loads(response.text)
    current_glance = (version for version in glance_versions['versions']
                      if version['status'] == 'CURRENT').next()
    glance_url = current_glance['links'][0]['href']
    response = sess.get('{}/images'.format(glance_url))
    image_list = json.loads(response.text)
    for image in image_list['images']:
        print (image)
        print ("******")

    # Here we retrieve a list of the instances in your project
    # Since the Nova API endpoint already includes a version, we
    # can just use it directly
    response = sess.get('{}/servers'.format(nova_url))
    server_list = json.loads(response.text)
    for server in server_list['servers']:
        print (server)
        print ("******")
