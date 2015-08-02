# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:32:07 2015

@author: nncanepa
"""

print('Please think of a number between 0 and 100!')
high=100
low=0
ans=(high + low)/2
state=''

while state != 'c':
    print('Is your secret number ' + str(ans) + '?')
    state=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if state=='h':
        high=ans
    elif state=='l':
        low=ans
    elif state=='c':
        break
    else:
        print('Sorry, I did not understand your input.')
    
    ans=(high + low)/2
        
print("Game over. Your secret number was:"),ans