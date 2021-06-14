#!usr/bin/env python
# -*- coding: utf-8 -*-
'''Week 5 - Assignment 1'''

import argparse
import time
import csv
import urllib2

parser = argparse.ArgumentParser()
parser.add_argument('--file', type = str, help = 'Files to process.')
parser.add_argument('--servers', type = int, help = 'Number of Servers.')
args = parser.parse_args()
servers = args.servers
servers = 10
test_url = 'http://s3.amazonaws.com/cuny-is211-spring2015/requests.csv'

if args.file is None:
    url = test_url
else:
    url = args.file

class Queue:
    ''' '''
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Server:
    ''' ''' 
    def __init__(self):        
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self,new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_length()

class Request:
    ''' '''
    def __init__(self, time, length):
        self.timestamp = time
        self.length = int(length)

    def get_stamp(self):
        return self.timestamp

    def get_length(self):
        return self.length

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulateOneServer(filename):
    server = Server()
    queue = Queue()
    wait_times = []
    data = urllib2.urlopen(filename)
    lstdata = list(csv.reader(data))
    lst = []
    task_start, count_start = 0,0

    for row in lstdata:
        lst.append(int(row[0]))
        row[0] = int(row[0])
        row[2] = int(row[2])
    ls_max = max(lst)

    while(task_start < len(lstdata)):
        if lstdata[task_start][0] == count_start:
            time_now = time.time()
            task = Request(time_now, lstdata[task_start][2])
            queue.enqueue(task)
            task_start = task_start + 1
        else:
            server.tick()
            count_start = count_start + 1
        if not queue.is_empty() and not server.busy():
            new_task = queue.dequeue()
            time_now = time.time()
            wait_times.append(new_task.wait_time(time_now))
            server.start_next(new_task)
    avg_wait_time = str(sum(wait_times)/len(wait_times))
    print ('Single Server:\nAverage wait time ' +
           avg_wait_time +' seconds.\nFor ' +
           str(len(wait_times)) + ' requests.')     

def simulateManyServers(filename, servers):
    server = Server()
    queue = Queue()
    wait_times = []
    data = urllib2.urlopen(filename)
    lstdata = list(csv.reader(data))
    lst = []
    serverlst = []
    task_start, count_start = 0,0

    for row in lstdata:
        lst.append(int(row[0]))
        row[0] = int(row[0])
        row[2] = int(row[2])
    ls_max = max(lst)

    for i in range(servers):
        serverlst.append(server)

    while(task_start < len(lstdata)):
        if lstdata[task_start][0] == count_start:
            time_now = time.time()
            task = Request(time_now, lstdata[task_start][2])
            if task_start == 0:
               server_start = 0
            else:
                server_start = task_start % servers
            serverlst[server_start].queue.enqueue(task)
            task_start = task_start + 1
        else:
            for row in serverlst:
                row.tick()
            count_start = count_start + 1

        for server in serverlst:
            if not server.busy() and not server.queue.is_busy():
                new_task = server.queue.dequeue()
                time_now = time.time()
                wait_time.append(new_task.wait_time(time_now))
                server.start_next(new_task)

    avg_wait_time = str(sum(wait_times)/len(wait_times))
    print ('Many Servers:\nAverage wait time ' +
           avg_wait_time +' seconds.\nFor ' +
           str(len(wait_times)) + ' requests.')

if __name__ == '__main__':
    if servers == 1 or servers is None:
        simulateOneServer(url)
    else:
        simulateManyServers(url, servers)
