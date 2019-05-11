# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:08:39 2019

@author: Aarav
"""

#import constructor
from constructor import calculator
#from random import randint
import random
class rand:
    def genRandom(self):
        x=calculator.a      
        y=calculator.b
        print("Random number generated: {}".format(random.randint(x,y)))
        

r=rand()
r.genRandom()



