# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:46:37 2015

@author: nncanepa
"""

class Queue(object):
    """ FIFO Queue implementation """
    def __init__(self):
        self.vals = []
    def insert(self, x):
        """ Agrega un elemento al final de la cola"""
        self.vals.append(x)
    def remove(self):
        """ Extrae el primer elemento de la cola """
        try:
            return self.vals.pop(0)
        except:
            raise ValueError()