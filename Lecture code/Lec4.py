# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:56:44 2015

@author: nncanepa
"""
s='uuuuuajbekjuhgikjhgokjhujhge'
vowels=0
for letter in s:
    if letter == 'a':
        vowels+=1
    if letter == 'e':
        vowels+=1
    if letter == 'i':
        vowels+=1
    if letter == 'o':
        vowels+=1
    if letter == 'u':
        vowels+=1
        
print('Number of vowels:'+ str(vowels))

x='uaj' in s