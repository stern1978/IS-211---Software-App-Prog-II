#!usr/bin/env python
# -*- coding: utf-8 -*-
'''Week 4 - Assignment 2'''

import time
import random

def insertion_sort(a_list):
    ''' '''
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position -1] > current_value:
            a_list[position] = a_list[position -1]
            position = position - 1
        a_list[position] = current_value
    end = time.time()
    duration = end - start
    return a_list, duration

def shell_sort(a_list):
    ''' '''
    start = time.time()
    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
        end = time.time()
        duration = end - start
        return a_list, duration

def gap_insertion_sort(a_list, start, gap):
    ''' '''
    for x in range(start + gap, len(a_list), gap):
        current_value = a_list[x]
        position = x
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value

def python_sort(a_list):
    ''' '''
    start = time.time()
    a_list = a_list.sort()
    end = time.time()
    duration = end - start
    return a_list, duration

def main():
    ''' '''
    msg = 'took %10.7f seconds to run, on average.'
    
    random1 = random.sample(xrange(500), 500)
    random2 = random.sample(xrange(1000), 1000)
    random3 = random.sample(xrange(10000), 10000)

    isort = 'Insertion Sort '
    ssort = 'Shell Sort '
    psort = 'Python Sort '

    total_time = 0

    for x in range(0, 100):
        found, time = insertion_sort(random1)
    for x in range(0, 100):
        found, time = insertion_sort(random2)
    for x in range(0, 100):
        found, time = insertion_sort(random3)
        total_time += time
    print isort + str(msg) % (total_time)

    total_time = 0

    for i in range(0, 100):
        found, time = shell_sort(random1)
    for x in range(0, 100):
        found, time = shell_sort(random2)
    for x in range(0, 100):
        found, time = shell_sort(random3)
        total_time += time
    print ssort + str(msg) % (total_time)

    total_time = 0

    for x in range(0, 100):
        found, time = python_sort(random1)
    for x in range(0, 100):
        found, time = python_sort(random2)
    for x in range(0, 100):
        found, time = python_sort(random3)
        total_time += time
    print psort + str(msg) % (total_time)

if __name__ == '__main__':
    main()
