#!usr/bin/env python
# -*- coding: utf-8 -*-
'''Week 6 - Assignment 2'''

absoluteZeroC = -273.15
absoluteZeroK = 0
absoluteZeroF = -459.66
mi_yard = 1760.0
mi_m = 1609.34
m_yard = 1.09361
yard_m = .9144
zeroError = 'Lower limit Error.  Input is less than Absolute Zero.'
numberError = 'Entry is not a number.'
canNotConvert = 'Can not convert these types.'
class LowerLimitError(Exception): pass
class NumberError(Exception): pass
class ConversionNotPossible(Exception): pass

conversion_dict = {
    ('celsius', 'kelvin'):('x + -273.15'),
    ('celsius', 'fahrenheit'):('x * 9.0/5.0 + 32'),
    ('fahrenheit', 'kelvin'):('x + (-459.66) * 5/2'),
    ('fahrenheit', 'celsius'):('(x - 32.0) * 5.0/9.0'),
    ('kelvin', 'fahrenheit'):('x * 9.0/5.0 + -495.66'),
    ('kelvin', 'celsius'):('x * 9.0/5.0 + -273.15'),
    ('mile', 'meter'):('x * 1609.34'),
    ('mile', 'yard'):('x * 1760.0'),
    ('meter', 'mile'):('x / 1609.34'),
    ('meter', 'yard'):('x * 1.09361'),
    ('yard', 'mile'):('x / 1609.34'),
    ('yard', 'meter'):('x * .9144')
    }

def convert(fromUnit, toUnit, value):
    if type(value) is not int:
        raise NumberError, numberError
    elif fromUnit == toUnit:
        return value
    #elif fromUnit and toUnit not in conversion_dict:
        #print fromUnit, toUnit, value, conversion_dict
        #raise ConversionNotPossible, canNotConvert
    elif (conversion_dict == 'kelvin' and value < absoluteZeroK or
          conversion_dict == 'celsius' and value < absoluteZeroC or
          conversion_dict == 'fahrenhight' and value < absoluteZeroF):
        raise LowerLimitError, zeroError
    else:
        x = value
        conversion = eval(conversion_dict[(fromUnit, toUnit)])
        return round(conversion, 2)


#print convert('yard', 'kelvin', 0)   
#print convert('celsius', 'kelvin', 100)
#print convert('celsius', 'fahrenheit', 100)
#print convert('fahrenheit', 'kelvin', 100)
#print convert('fahrenheit', 'celsius', 100)
#print convert('kelvin', 'fahrenheit', 100)
#print convert('kelvin', 'celsius', 100)
#print convert('mile', 'meter', 100)
#print convert('mile', 'yard', 100)
#print convert('meter', 'mile', 100)
#print convert('meter', 'yard', 100)
#print convert('yard', 'mile', 100)
#print convert('yard', 'meter', 100)
#print convert('yard', 'yard', 10)
