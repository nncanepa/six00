# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:44:18 2015

MITx 6.00x

PSET2 - Part3


        Test Case 1:
	      balance = 320000
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 29157.09
       
        Test Case 2:
	      balance = 999999
	      annualInterestRate = 0.18
	      
	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 90325.03
@author: nncanepa

"""


balance = 999999
annualInterestRate = 0.18


low = balance/12.0
high = (balance*(1+(annualInterestRate/12.0))**12)/12.0
payment=(high + low)/12.0

def balanceAnual(balance,payment,annualInterestRate):
    '''
    Returns balance afer 12 month, given current balance, annual interest and monthly payment
    '''
    for i in range(12):
        balance=(balance-payment)*(1 + (annualInterestRate/12.0))
    return balance



while round(balanceAnual(balance,payment,annualInterestRate),2) != 0:

    if round(balanceAnual(balance,payment,annualInterestRate),2) > 0:
        low=payment
    elif round(balanceAnual(balance,payment,annualInterestRate),2) < 0:
        high=payment
    payment=(high+low)/2
    
print 'Lowest Payment: ' + str(round(payment,2))
#print 'Termino pagando: ' + str(round(payment,2)*12)
