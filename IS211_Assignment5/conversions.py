#!usr/bin/env python
# -*- coding: utf-8 -*-
'''Week 5 - Assignment 1'''

absoluteZero = -273.15
#zeroError = raise LowerLimitError, 'Lower limit Error.  Input is less than Absolute Zero.'

def convertCelsiusToKelvin(input):
    if input < -273.15:
        raise LowerLimitError, 'Lower limit Error.  Input is less than Absolute Zero.'
        #raise zeroError
    else:
        return round(input + absoluteZero, 2)

def convertCelsiusToFahrenheit(input):
    if input < absoluteZero:
        raise zeroError
    else:
        return round(input * 9.0/5.0 + 32.0, 2)
    
