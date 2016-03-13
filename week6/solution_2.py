import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

location = raw_input('Enter location: ')
#url with address
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': location})
print 'Retrieving', url
#process data
data = urllib.urlopen(url)
read_data = data.read()
#length of reftrieved data
print 'Retrieved',len(read_data),'characters'

try: process_json = json.loads(str(read_data))
except: process_json = None
if 'status' not in process_json or process_json['status'] != 'OK':
    print '==== Failure To Retrieve ===='
    print read_data

#Get the Place ID
place_id = process_json['results'][0]['place_id']
print 'Place id:', place_id
