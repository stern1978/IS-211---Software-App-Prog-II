#!usr/bin/env python
# -*- coding: utf-8 -*-
'''Week 4 - Assignment 1'''

import random
import time

def sequential_search(alist, item):
    ''' '''
    start = time.time()
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    end = time.time()
    duration = end - start
    return found, duration

def ordered_sequential_search(alist, item):
    ''' '''
    start = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist [pos] == item:
            found = True
        else:
            pos += 1
    end = time.time()
    duration = end - start
    return found, duration

def binary_search_iterative(alist, item):
    ''' '''
    start = time.time()
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint - 1
                
    end = time.time()
    duration = end - start
    return found, duration    

def binary_search_recursive(alist, item):
    ''' '''
    start = time.time()
    if len(alist) == 0:
        found = False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                return binary_search_recursive(alist[:midpoint], item)
            else:
                return binary_search_recursive(alist[midpoint + 1:], item)
    end = time.time()
    duration = end - start
    return found, duration

def main():
    ''' '''
    msg = 'took%10.7f seconds to run, on average.'
    
    random1 = random.sample(xrange(500), 500)
    random2 = random.sample(xrange(1000), 1000)
    random3 = random.sample(xrange(10000), 10000)

    ss = 'Sequential Search '
    oss = 'Ordered Sequential Search '
    bsi = 'Binary Search Iterative '
    bsr = 'Binary Search Recursive '

    total_time = 0

    for x in range(0, 100):
        found, time = sequential_search(random1, -1)
        total_time += time
    for x in range(0, 100):
        found, time = sequential_search(random2, -1)
        total_time += time
    for x in range(0, 100):
        found, time = sequential_search(random3, -1)
        total_time += time
    print ss + str(msg) % (total_time)

    total_time = 0

    for x in range(0, 100):
        found, time = ordered_sequential_search(random1, -1)
        total_time += time
    for x in range(0, 100):
        found, time = ordered_sequential_search(random2, -1)
        total_time += time
    for x in range(0, 100):
        found, time = ordered_sequential_search(random3, -1)
        total_time += time
    print oss + str(msg) % (total_time)

    total_time = 0

    for x in range(0, 100):
        found, time = binary_search_iterative(random1, -1)
        total_time += time
    for x in range(0, 100):
        found, time = binary_search_iterative(random2, -1)
        total_time += time
    for x in range(0, 100):
        found, time = binary_search_iterative(random3, -1)
        total_time += time
    print bsi + str(msg) % (total_time)

    total_time = 0

    for x in range(0, 100):
        found, time = binary_search_recursive(random1, -1)
        total_time += time
    for x in range(0, 100):
        found, time = binary_search_recursive(random2, -1)
        total_time += time
    for x in range(0, 100):
        found, time = binary_search_recursive(random3, -1)
    print bsr + str(msg) % (total_time)

if __name__ == '__main__':
    main()
