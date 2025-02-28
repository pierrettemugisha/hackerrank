#!/bin/python3


#
# https://www.hackerrank.com/challenges/day-of-the-programmer/problem
#

def dayOfProgrammer(year):
    # Write your code here
    if year == 1918:
        return '26.09.1918'
    elif year > 1918:  # Gregorian calendar
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'
    else:  # Julian calendar
        if year % 4 == 0:
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'
