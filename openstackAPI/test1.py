from keystoneauth1 import identity
from keystoneauth1 import session
from novaclient import client

auth = identity.v3.oidc.OidcPassword(
    'https://kaizen.massopen.cloud:5000/v3',
    identity_provider='moc',
    protocol='openid',
    client_id='kaizen-client',
    client_secret='fac377a9-f2ba-41e7-bb7f-4064dd9f4468',
    access_token_endpoint='https://sso.massopen.cloud/auth/realms/moc/protocol/openid-connect/token',
    discovery_endpoint='https://sso.massopen.cloud/auth/realms/moc/.well-known/openid-configuration',
    username='asan@bu.edu',
    password='doNOTuseMYaccount',
    project_name='BU_CCC18_CDN_and_WAF',
    project_domain_name='Default'
)
s = session.Session(auth)

nova = client.Client(version=2, session=s)
print(nova.flavors.list())
