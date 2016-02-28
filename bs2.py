import urllib
import re
from bs4 import BeautifulSoup

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
# converting coount to int to process it
count = int(count)
position = raw_input('Enter position: ')
# converting position to int to process it
position = int(position)

# repeat count number of times
for i in range(0, count+1):

    # read url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    # print retrieving urls by entered count
    if i < count:
        print 'Retrieving: ', url
    else:
        print 'Retrieving: ', url
        break

    # Get all anchor tags
    tags = soup('a')

    # find the tag at position
    tag_position = 0
    for tag in tags:
        if tag_position == position-1:
            url = str(tag.get('href', None))
            break
        tag_position += 1
