# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:38:41 2015

@author: nncanepa
"""

#def iterPower(base, exp):
#    result=1
#    if (type(exp) != type(1)) or exp < 0:
#        print 'exp must be a positive integer'
#    elif type(exp) == type(1) and exp >= 0:
#        while exp > 0:
#            result *= base
#            exp -= 1
#        return result
#
#def recurPower(base, exp):
#    assert exp >= 0 and type(exp) == int
#    if exp == 1:
#        return base
#    elif exp == 0:
#        return 1
#    else:
#        return base*recurPower(base,exp-1)
#        
#def recurPowerNew(base, exp):
#    if exp == 0:
#        return 1
#    elif exp%2 == 0:
#        return recurPowerNew(base*base,exp/2) 
#    else:
#        return base*recurPowerNew(base,exp-1)
#        
#def gcdIter(a, b):
#    div=min(a,b)
#    while div >1:
#        if a%div == 0 and b%div == 0:
#            return div
#        else:
#            div -= 1
#    return div
#    
#def gcdRecur(a,b):
#    if b == 0:
#        return a
#    else:
#        return gcdRecur(b,a%b)
#        
#def lenIter(aStr):
#    ans=0
#    for c in aStr:
#        ans += 1
#    return ans
#    
#    
#def lenRecur(aStr):
#    if aStr=='':
#        return 0
#    elif aStr[:-1] == '':
#        return 1
#    else:
#        return 1 + lenRecur(aStr[:-1])
#        
#        
def isIn(char, aStr):
    if aStr == '':
        return False
    elif len(aStr) == 1:
        return char == aStr
    elif char == aStr[int(round(len(aStr)/2))]:
        return True
    elif char < aStr[int(round(len(aStr)/2))]:
        return isIn(char, aStr[0:int(round(len(aStr)/2))])
    elif char > aStr[int(round(len(aStr)/2))]:
        return isIn(char, aStr[int(round(len(aStr)/2)):])


def semordnilap(str1, str2):
    if len(str1) != len(str2):
        return False
    elif str1 == '':
        return True
    elif str1[0] == str2[-1]:
        return True and semordnilap(str1[1:], str2[:-1])
    else:
        return False    

def semordnilapWrapper(str1, str2):
        
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False
        
        
    return semordnilap(str1, str2)
    