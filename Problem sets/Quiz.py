# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 15:03:00 2015

@author: Nicolas Canepa
"""

def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    y=0
    while b**y <= x:
        y += 1
    return y-1
    
aList = ["apple", "cat", "dog", "banana","gato"]

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    lista = []
    for string in aList:
        if len(string) < 4:
            lista.append(string)
    return lista
    
def sumDigits(N):
    '''
    Given an integer returns the sum of the digits
    N: a non-negative integer
    '''
    if N == 0:
        return 0
    else:
        return sumDigits(N/10) + N%10
        
        
aDict={1:10,2:20,7:70,4:67}        
        
def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    keys=aDict.keys()
    result=[]
    for key in keys:
        if aDict[key] == target:
            result.append(key)
    result.sort()
    return result
    
    
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    localL=L[:]
    for el1 in localL:
        if not(f(el1)):
            L.remove(el1)
    return len(L)
    


#run_satisfiesF(L, satisfiesF)

def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print satisfiesF(L)
print L
