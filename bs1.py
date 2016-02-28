import urllib
import re
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup.findAll('span', {'class' : 'comments'})
total = 0
for tag in tags:
    # Look at the parts of a tag
    nums = str(tag)
    x = re.findall('[0-9]+', nums)
    if len(x) > 0:
        for item in x:
            total += int(item)

print 'Count', len(tags)
print 'Sum', total
