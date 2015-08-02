# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 13:29:48 2015

@author: nncanepa
"""

#s = 'azcbobobegghakl'   # Resultado esperado 'beggh'


# String para probar que solo imprima la primer coincidencia si hay empate
#s = 'abcbcd'

s = 'leyrctjw'  #*** ERROR: Expected 'ey', got 'ct'. ***
#s = 'olvenzgezfphqhsmhahgmq'
#s = 'pdabqiysomec'
#s = 'adkahiaqesbyfgykmezxiqp'

abc='abcdefghijklmnopqrstuvwxyz'
result=s[0]
index=0
y=0
d=[]
dd=''

while index < (len(s)-1):
    
    y=abc.find(s[index]) #Valor numerico en el alfabeto
    if y <= abc.find(s[index+1]):
        result+=s[index+1]
    else:
        d.append(result)
        result=s[index+1]        
    index+=1

d.append(result)
dd=d[0]
for i in range(0,len(d)-1):
    if len(d[i])<len(d[i+1]):
        if len(dd)<len(d[i+1]):
            dd=d[i+1]
        
        
print 'Longest substring in alphabetical order is: ' + str(dd)

