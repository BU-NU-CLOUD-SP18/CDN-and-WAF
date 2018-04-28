#!/usr/bin/env bash
export OS_AUTH_URL="https://kaizen.massopen.cloud:5000/v3"
export OS_USERNAME="asan@bu.edu"
export OS_PROJECT_NAME="BU_CCC18_CDN_and_WAF"
export OS_PROJECT_DOMAIN_NAME="Default"
echo "Please enter your SSO Password for project $OS_PROJECT_NAME as user $OS_USERNAME: "
read -sr OS_PASSWORD_INPUT
export OS_PASSWORD=$OS_PASSWORD_INPUT
export OS_REGION_NAME="MOC_Kaizen"
export OS_AUTH_TYPE="v3oidcpassword"
export OS_IDENTITY_PROVIDER="moc"
export OS_PROTOCOL="openid"
export OS_CLIENT_ID="kaizen-client"
export OS_CLIENT_SECRET="fac377a9-f2ba-41e7-bb7f-4064dd9f4468"
export OS_ACCESS_TOKEN_ENDPOINT="https://sso.massopen.cloud/auth/realms/moc/protocol/openid-connect/token"
export OS_DISCOVERY_ENDPOINT="https://sso.massopen.cloud/auth/realms/moc/.well-known/openid-configuration"
export OS_INTERFACE=public
export OS_IDENTITY_API_VERSION=3
