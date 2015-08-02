# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:05:37 2015

@author: nncanepa
"""

#s='bobobobobobobobobob'

# Casos que fallaron:
s='bobobobobobobobobob'     #*** ERROR: Expected 9, got 8. ***
#s = 'bobbbobobboobooboob'   #*** ERROR: Expected 3, got 2. ***


where=0
count=0
if 'bob' in s:
    while True:
        where=s.find('bob',where)
        if where!=-1:
            count+=1
        if where==-1:
            break
        where+=1
print 'Number of times bob occurs is: '+str(count)