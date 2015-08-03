# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 14:40:39 2015

@author: Administrador
"""

import string

#s='Soft!" he exclaimed as he threw the football.'
s='Microsoft recently released the Windows 8 Consumer Preview.'
s=s.lower()

for char in string.punctuation:
    s = s.replace(char, '')

triggers=['soft']

found = False

for word in s.split():
    print word
    if word in triggers:
        #print "HOLAAAA"
        found = True
        break
    else:
        found = False
        
print found