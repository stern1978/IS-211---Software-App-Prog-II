#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 2 - Assignment 1"""

import urllib2

testurl = urllib2.urlopen('https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv')
url=testurl

def downloadData(url):
    urlin = urllib2.urlopen(url)
    print urlin.read()
    return urlin

def processData(data):

    print data
    return data

def displayPerson(id, personData):

    print id
    return id

downloadData(url)
