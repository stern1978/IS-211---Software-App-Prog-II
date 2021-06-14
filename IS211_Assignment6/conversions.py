#!usr/bin/env python
# -*- coding: utf-8 -*-
'''Week 6 - Assignment 1'''

absoluteZeroC = -273.15
absoluteZeroK = 0
absoluteZeroF = -459.66
zeroError = 'Lower limit Error.  Input is less than Absolute Zero.'
class LowerLimitError(Exception): pass

def convertCelsiusToKelvin(input):
    if input < absoluteZeroC:
        raise LowerLimitError, zeroError
    else:
        return round(input + absoluteZeroC, 2)

def convertCelsiusToFahrenheit(input):
    if input < absoluteZeroC:
        raise LowerLimitError, zeroError
    else:
        return round(input * 9.0/5.0 + 32.0, 2)
    
def convertFahrenheitToKelvin(input):
    if input < absoluteZeroF:
        raise LowerLimitError, zeroError
    else:
        return round(input + (-absoluteZeroF) * 5/2, 2)

def convertFahrenheitToCelsius(input):
    if input < absoluteZeroF:
        raise LowerLimitError, zeroError
    else:
        return round((input - 32.0) * 5.0/9.0, 2)
    
def convertKelvinToFahrenheit(input):
    if input < absoluteZeroK:
        raise LowerLimitError, zeroError
    else:
        return round(input * 9.0/5.0 + absoluteZeroF, 2)

def convertKelvinToCelsius(input):
    if input < absoluteZeroK:
        raise LowerLimitError, zeroError
    else:
        return round(input * 9.0/5.0 + absoluteZeroC, 2)
