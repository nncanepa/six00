# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 17:25:18 2015

@author: nncanepa
"""

def square(x):
    return x*x
#    
#def evalQuadratic(a,b,c,x):
#    return (a*x*x+b*x+c)
#    
#def f(x):
#    y=1
#    x=x+y
#    print 'hoola: ' + str(x)
#    return x
#    
#def clip(lo, x, hi):
#    return max(lo,min(x,hi))
#    
#def nico(x,a):
#    a=10+a
#    return x+a

def fourthPower(x):
    return square(square(x))
    
def odd(x):
    return bool(abs(x)%2)
    
def isVowel2(char):
    return char in 'aeiouAEIOU'
    
def isVowel(char):
    return char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u'