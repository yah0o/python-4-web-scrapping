import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
print 'Retrieving', url
processed_url = urllib.urlopen(url)
data = processed_url.read()
print 'Retrieved', len(data), 'characters'
tree = ET.fromstring(data)
counts = tree.findall('.//comment')
print 'Count:', len(counts)
total = 0                                       #set sum value to 0
for item in counts:                             #iterate list of comments
    find_element = item.find('count').text      #find element <count>
    total = total + int(find_element)           #add integer value to total

print 'Sum:', total
