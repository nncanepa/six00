# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 16:48:43 2015

@author: nncanepa
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    nDict = {}
    for i in aDict.keys():
        if not (aDict[i] in nDict.values()):
            nDict[i]=aDict.pop(i)
    for i in nDict.keys():
        if nDict[i] in aDict.values():
            nDict.pop(i)
    return sorted(nDict.keys())

aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
aDict2 = {}