import json
import urllib

url = raw_input('Enter location: ')
print 'Retrieving', url
processed_url = urllib.urlopen(url)
data = processed_url.read()
print 'Retrieved', len(data), 'characters'

info = json.loads(data) #process json
print 'Count:', len(info['comments']) #get count

#Get total amount of elements 'count'
total = 0
for i in info['comments']: 
    total = total + i['count']

print 'Sum:', total
