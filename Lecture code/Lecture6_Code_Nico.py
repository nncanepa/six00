# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 11:32:43 2015

@author: nncanepa
"""

def oddTuples(aTup):
    nTup = ()
    for i in range(len(aTup)):
        if i%2 == 0:
            nTup = nTup + (aTup[i],)
    return nTup
            
def oddTuples2(aTup):
    return aTup[::2]
    
    
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
testList = [1, -4, 8, -9]

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result


def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1
    
    
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def howMany(aDict):
    sum = 0
    for j in aDict:
        for k in aDict[j]:
            sum += 1
    return sum
    
def biggest(aDict):
    tam=0
    k=''
    if len(aDict) == 0:
        return None
    for j in aDict:
        if len(aDict[j]) >= tam:
            tam=len(aDict[j])
            k = j
    return k