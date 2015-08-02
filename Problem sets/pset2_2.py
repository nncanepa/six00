# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:44:48 2015
MITx 6.00x

PSET2 - Part 2

	  Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310
       
       
       Test Case 2:
	      balance = 4773
	      annualInterestRate = 0.2
	      
	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 440
       
       Test Case 3:
	      balance = 3926
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 360



@author: nncanepa
"""

balance = 4773.0
annualInterestRate = 0.2

payment = 0
balance2 = 0.0

def balanceMonth(balance,payment,annualInterestRate):
    '''
    Devuelve el balance actual dado el balance anterior y el pago efectuado.
    '''
    return (balance-payment)*(1 + (annualInterestRate/12.0))


while balance2 >= 0: 
    payment += 10
    balance2=balance
    for i in range(12):
        balance2 = balanceMonth(balance2,payment,annualInterestRate)        

print 'Lowest Payment: ' + str(payment)