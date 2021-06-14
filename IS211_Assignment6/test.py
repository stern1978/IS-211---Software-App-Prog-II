#!usr/bin/env python
# -*- coding: utf-8 -*-
'''Week 6 - Assignment 3'''

import conversions
#import conversions_refactored
import unittest

class kelvinTest(unittest.TestCase):
    def testKelvinCelsius(self):
        self.testval = ((0.00, -273.15),
                    (63.15,-210.00),
                    (123.15, -150.00),
                    (193.15, -80.00),
                    (243.15, -30.00),
                    (323.15, 50),
                    (393.15, 120.00),
                    (483.15, 210.00))
        for k, c in self.testval:
            test = conversions.convertKelvinToCelsius(k)
            self.assertTrue(test, c)

    def testKelvinFahrenheit(self):
        self.testval = ((0.00, -459.67),
                   (63.15,-346.00),
                   (123.15, -238.00),
                   (193.15, -112.00),
                   (243.15, -22.00),
                   (323.15, 122.00),
                   (393.15, 248.00),
                   (483.15, 410.00))
        for k, c in self.testval:
            test = conversions.convertKelvinToFahrenheit(k)
            self.assertTrue(test, c)

class celsiusTest(unittest.TestCase):
    def testCelsiusKelvin(self):
        self.testval = ((-273.15, 0),
                        (-260,13.15),
                        (-200,73.15),
                        (-160, 113.15),
                        (-100, 173.15),
                        (0,273.15),
                        (50,323.15),
                        (100,373.15),
                        (200,473.15),
                        (250,523.15),
                        (300,573.15))
        for k, c in self.testval:
            test = conversions.convertCelsiusToKelvin(k)
            self.assertTrue(test, c)

    def testCelsiusFahrenheit(self):
        self.testval = ((-273.15,-459.67),
                        (-180.00, -292.00),
                        (-20.00, -4.00),
                        (0.00, 32.00),
                        (30.00, 86.00),
                        (100.00, 212.00),
                        (300.00, 572.00))
        for k, c in self.testval:
            test = conversions.convertCelsiusToFahrenheit(k)
            self.assertTrue(test, c)

class fahrenheitTest(unittest.TestCase):
    def testFahrenheitKelvin(self):
        self.testval = ((-459.67,0.00),
                        (-364.00,53.15),
                        (-202.00, 143.15),
                        (-130.00, 183.15),
                        (-22.00, 243.15),
                        (86.00, 303.15),
                        (212.00, 373.15),
                        (392.00,473.15))
        for k, c in self.testval:
            test = conversions.convertFahrenheitToKelvin(k)
            self.assertTrue(test, c)

    def testFahrenheitCelsius(self):
        self.testval = ((-459.67,-273.15),
                        (-292.00,-180.00),
                        (-94.00, -70.00),
                        (-4.00, -20.00),
                        (32.00, 0.00),
                        (86.00, 30.00),
                        (176.00, 80.00),
                        (284.00,140.00),
                        (572.00, 300))
        for k, c in self.testval:
            test = conversions.convertFahrenheitToCelsius(k)
            self.assertTrue(test, c)

if __name__ == '__main__':
    unittest.main()
