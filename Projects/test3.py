import json, requests

url = 'https://sqm.freshdesk.com/api/v2/tickets'

params = dict(
    APIkey='hFwt7OujS1XIQqL1r13',
    password='xxxx'
)

proxies = {'https': 'http://sqmdom\\rmark:A10nitratos@clsclisaw01.sqm.local:8080/'}

resp = requests.get(url=url, proxies=proxies, headers={'Authorization': 'APIkey:hFwt7OujS1XIQqL1r13'})
data = json.loads(resp.text)

print(data)
