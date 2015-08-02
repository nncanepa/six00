# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:05:26 2015

MITx 6.00x
PSET 2 - Part 1

Test Case 1:
	      balance = 4213
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04
	      
	      Result Your Code Should Generate:
	      -------------------
	      Month: 1
	      Minimum monthly payment: 168.52
	      Remaining balance: 4111.89
	      Month: 2
	      Minimum monthly payment: 164.48
	      Remaining balance: 4013.2
	      Month: 3
	      Minimum monthly payment: 160.53
	      Remaining balance: 3916.89
	      Month: 4
	      Minimum monthly payment: 156.68
	      Remaining balance: 3822.88
	      Month: 5
	      Minimum monthly payment: 152.92
	      Remaining balance: 3731.13
	      Month: 6
	      Minimum monthly payment: 149.25
	      Remaining balance: 3641.58
	      Month: 7
	      Minimum monthly payment: 145.66
	      Remaining balance: 3554.19
	      Month: 8
	      Minimum monthly payment: 142.17
	      Remaining balance: 3468.89
	      Month: 9
	      Minimum monthly payment: 138.76
	      Remaining balance: 3385.63
	      Month: 10
	      Minimum monthly payment: 135.43
	      Remaining balance: 3304.38
	      Month: 11
	      Minimum monthly payment: 132.18
	      Remaining balance: 3225.07
	      Month: 12
	      Minimum monthly payment: 129.0
	      Remaining balance: 3147.67
	      Total paid: 1775.55
	      Remaining balance: 3147.67


 Test Case 2:
	      balance = 4842
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04
	      
	      Result Your Code Should Generate:
	      -------------------
	      Month: 1
	      Minimum monthly payment: 193.68
	      Remaining balance: 4725.79
	      Month: 2
	      Minimum monthly payment: 189.03
	      Remaining balance: 4612.37
	      Month: 3
	      Minimum monthly payment: 184.49
	      Remaining balance: 4501.68
	      Month: 4
	      Minimum monthly payment: 180.07
	      Remaining balance: 4393.64
	      Month: 5
	      Minimum monthly payment: 175.75
	      Remaining balance: 4288.19
	      Month: 6
	      Minimum monthly payment: 171.53
	      Remaining balance: 4185.27
	      Month: 7
	      Minimum monthly payment: 167.41
	      Remaining balance: 4084.83
	      Month: 8
	      Minimum monthly payment: 163.39
	      Remaining balance: 3986.79
	      Month: 9
	      Minimum monthly payment: 159.47
	      Remaining balance: 3891.11
	      Month: 10
	      Minimum monthly payment: 155.64
	      Remaining balance: 3797.72
	      Month: 11
	      Minimum monthly payment: 151.91
	      Remaining balance: 3706.57
	      Month: 12
	      Minimum monthly payment: 148.26
	      Remaining balance: 3617.62
	      Total paid: 2040.64
	      Remaining balance: 3617.62
@author: nncanepa
"""

balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02
totalPayment = 0.0

def balanceMonth(b,air,mpr):
    """
    Devuelve el balance mensual actual dado el balance anterior, el pago efectuado,
    el interes anual, y el rate de pago mensual
    """
    return ((b-mpr*b)*(1+(air/12.0)), mpr*b)
    
for i in range(12):
    (balance,mp)=balanceMonth(balance,annualInterestRate,monthlyPaymentRate)
    totalPayment += mp
    print 'Month:' + str(i+1)
    print 'Minimun monthly payment: ' + str(round(mp,2))
    print 'Remaining balance: ' + str(round(balance,2))

totalPayment = round(totalPayment,2)
print 'Total paid: ' + str(totalPayment)
print 'Remaining balance: ' + str(round(balance,2))

