# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 10:39:51 2015

@author: nncanepa
"""

#def testNico(lista, numero):
#    return [[elt[0], elt[1], numero] for elt in lista]
#    
#    
#lista=[['Nico', 'Canepa'], ['Alberto', 'Peres'], ['Jose Luis','Peralez']]
#numero = 4
#
#result=testNico(lista, numero)



def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]


#def SimpleDivide(item, denom):
#   return item / denom
   
def SimpleDivide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0