# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 20:03:30 2015

@author: nncanepa
"""
#import numpy as np
#import matplotlib.pyplot as plt
#
#x=np.arange(0.1,7.0,0.1)
#
#
#for i in range(1,5):
#    y=np.sin(x)**i
#    plt.subplot(int('22'+str(i)))
#    if i == 1:
#        plt.plot(x,y,'r')
#    if i == 2:
#        plt.plot(x,y,'g')
#    if i == 3:
#        plt.plot(x,y,'b')
#    if i== 4:
#        plt.plot(x,y,'ro')
        
        
def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    while x >= a:
        count += 1
        x = x - a
    return count
    
    
def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        rem(x-a, a)
        
def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n+1
   else:
      return n * f(n-1)
      
      