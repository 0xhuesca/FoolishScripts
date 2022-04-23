
# URL hosting geolocalization 
# Requirement: pip3 install ip2geotools 
# Usage: python3 geoloc_url.py


import socket
from ip2geotools.databases.noncommercial import DbIpCity
location={}
_url= input("Enter the URL here: ")
try:
    if ("://" in _url):
        protocol, url = _url.split('://')
    else:
        url = _url
    _ip=socket.gethostbyname(url)
except:
     raise SystemExit("Wrong url value")
api_response = DbIpCity.get(_ip, api_key='free',)
location["IP"] = _ip
location["City"] = api_response.city
location["Region"] = api_response.region
location["Country"] = api_response.country
print(location)
