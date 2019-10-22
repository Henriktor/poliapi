import requests
import json
#import dictitems
from datetime import date


today = date.today()
d1 = today.strftime("%Y-%m")
print(d1)


payload = {'locationname': 'Malmö', 'DateTime' : d1}
resp = requests.get('https://polisen.se/api/events',params=payload)
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError(' error'.format(resp.status_code))
print (resp.url)
resp_dict = resp.json()
print('Händelser', + len(resp_dict))
for dict_item in resp_dict:
    print('\n' + 'Händelse')
    print (dict_item['location']['name'],dict_item['datetime'],dict_item['summary'])

#file = open("resp_text.txt", "w")
#file.write(resp.text)
#file.close()
    
