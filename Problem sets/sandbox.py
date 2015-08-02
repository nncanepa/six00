# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:50:44 2015

@author: nncanepa
"""

s = 'azcbobobegghakl'

vowels = 'aeiou'

count = 0

for char in s:
    if char in vowels:
        count += 1
    
print 'Number of vowels: ' + str(count)