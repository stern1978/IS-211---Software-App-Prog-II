#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 3 - Assignment 1"""

import argparse
import csv
import datetime
import operator
import re
import urllib2
import datetime

#url = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'
parser = argparse.ArgumentParser()
parser.add_argument('--url')
args = parser.parse_args()
url = args.url
url_data = urllib2.urlopen(url)
csvdata = cvs.reader(url_data)

browserhits = 0
imghits = 0
totalhits = 0
safari = chrome = firefox = msie = other = 0
dateformat = '%Y-%m-%d %H:%M:%S'
imagetype = ('.jpeg|.jpg|.gif|.png')
for row in csvdata:
    #print row
    totalhits += 1
    #print totalhits
    dataformat = {'path':row[0], 'date':row[1], 'browser':row[2], 'status':[3], 'size':row[4]}

    if re.search('firefox', dataformat['browser']):
        firefox += 1
    elif re.search('chrome/\d+', dataformat['browser']):
        chrome += 1
    elif re.search('mise', dataformat['browser']):
        msie += 1
    elif re.search('safari', dataformat['browser']):
        safari += 1
    elif re.search(imagetype, dataformat['path']):
        imgmatch += 1
    else:
        if not re.search(imagetype, dataformat['path']):
            other += 1

list = [("Firefox", firefox),("Chrome", chrome),("Internet Explorer", mise),("Safari", safari),("Other",other)]
topbrowser = sorted(list, key=operator.itemgetter(1), reverse = 1)[0][0]

print 'Total of image searches for per site is: %2.2f%%' % (imgmatch/totalhits)
print 'The top website used is %s' % topbrowser
