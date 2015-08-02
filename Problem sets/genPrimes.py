# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 12:16:47 2015

@author: nncanepa
"""

def genPrimes():
    n = 2
    primes = []
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
            yield n
        n += 1
        
        
## Numeral
        
def genNumeral():
    n = 1
    num =1 
    while True:
        for p in range(1,n):
            num *= p
        yield num
        n += 1
        num =1