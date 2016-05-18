import json, requests

urlpat = 'https://sqm.freshdesk.com/api/v2/tickets.json?updated_since=2015-01-01&per_page=20&page={0}'

urlpatgroup = 'https://sqm.freshdesk.com/api/v2/groups'
params = dict(
    APIkey='hFwt7OujS1XIQqL1r13',
    password='xxxx'
)

proxies = {'https': 'http://sqmdom\\rmark:A10nitratos@clsclisaw01.sqm.local:8080/'}
"""
resp = requests.get(url=url, headers={'Authorization': 'APIkey:hFwt7OujS1XIQqL1r13'})
data = json.loads(resp.text)
"""

ListTickets = []
page = 1
while (True):
    url = urlpat.format(str(page))
    r = requests.get(url, auth=("hFwt7OujS1XIQqL1r13", "X"))
    if (len(r.text)<=2):
        break;
    ListTickets+=r.json()

    page+=1

for i in ListTickets:
    print ('id : ' + str(i['id']))
    print ('priority : ' + str(i['priority']))
    print ('status : ' + str(i['status']))
    print ('subject : ' + str(i['subject'].encode('utf-8')))
    if (i['type']):
        print ('type : ' + str(i['type'].encode('utf-8')))
    if (i['custom_fields']['mdulo_sap']):
        print ('custom_fields\mdulo_sap : ' + str(i['custom_fields']['mdulo_sap'].encode('utf-8')))
"""
        created_at
        updated_at
        due_by
"""
