# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 14:40:39 2015

@author: Administrador
"""

import string

#s='Soft!" he exclaimed as he threw the football.'
s='Microsoft recently released the Windows 8 Consumer Preview.'
#s=s.lower()
#
#for char in string.punctuation:
#    s = s.replace(char, '')
#
#triggers=['soft']
#
#found = False
#
#for word in s.split():
#    print word
#    if word in triggers:
#        #print "HOLAAAA"
#        found = True
#        break
#    else:
#        found = False
#        
#print found



        
class WordTrigger(object):
    def __init__(self, word):
        self.word = word
    
    def removeSymbols(self,text):
        for char in string.punctuation:
            text = text.replace(char, ' ')
        return text
    
    def isWordIn(self,text):
        text=self.removeSymbols(text.lower())
        for word in text.split():
            if self.word in text:
                return True
            else:
                return False