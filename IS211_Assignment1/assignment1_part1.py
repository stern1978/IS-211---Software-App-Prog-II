#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 1 - Assignment 1"""

class ListDivideException(Exception):
    """Raises an exception"""

def listDivide(numbers, divide=2):
    """Returns the total number of a list of numbers divisable by divide.
    Args:
        numbers(list): a list of numbers
        divide(intiger): an intiger to divide by
    
    Return:
        The total from numbers divisable by divide
    
    Examples:
        listDivide([1, 2, 3, 4, 5])
        2

        listDivide([2, 4, 6, 8, 10])
        5
    
        listDivide([30, 54, 63, 98, 100], divide=10)
        2
    
        listDivide([])
        0
    
        listDivide([1, 2, 3, 4, 5], 1)
        5
    """
    dcount = 0
    for i in numbers:
        if i % divide == 0:
            dcount += 1
        else:
            continue
    return dcount

def testListDivide():
    """Test for listDivide"""
    test1 = listDivide([1, 2, 3, 4, 5])
    ans1 = 2
    test2 = listDivide([2, 4, 6, 8, 10])
    ans2 = 5
    test3 = listDivide([30, 54, 63, 98, 100], divide=10)
    ans3 = 2
    test4 = listDivide([])
    ans4 = 0
    test5 = listDivide([1, 2, 3, 4, 5], 1)
    ans5 = 5

    for i in range(5):
        num = str(i+1)
        test = eval('test' + num)
        ans = eval('ans' + num)
        if test != ans:
            raise ListDivideException('Error in code!!')
        else:
            continue

testListDivide()
