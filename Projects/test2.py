import json, requests

url = 'http://maps.googleapis.com/maps/api/directions/json'

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)

proxies = {'http': 'http://sqmdom\\rmark:A10nitratos@clsclisaw01.sqm.local:8080/'}

resp = requests.get(url=url, params=params, proxies=proxies)
data = json.loads(resp.text)

print(data)
