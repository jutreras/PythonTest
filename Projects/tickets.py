import json, requests

url = 'https://sqm.freshdesk.com/api/v2/tickets.json'

params = dict(
    APIkey='hFwt7OujS1XIQqL1r13',
    password='xxxx'
)

proxies = {'https': 'http://sqmdom\\rmark:A10nitratos@clsclisaw01.sqm.local:8080/'}
"""
resp = requests.get(url=url, headers={'Authorization': 'APIkey:hFwt7OujS1XIQqL1r13'})
data = json.loads(resp.text)
"""

r = requests.get(url, auth=("hFwt7OujS1XIQqL1r13", "X"))

print ('HTTP response code: ' + str(r.status_code))
print ('HTTP response body: ' + str(r.content))

"""print(data)"""
