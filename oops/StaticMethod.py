# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:55:27 2019

@author: Aarav
"""
'''
class Mathematics:
    
    def addNumbers(x,y):
        return x+y
    
Mathematics.addNumbers=staticmethod(Mathematics.addNumbers)
print("The sum is : ", Mathematics.addNumbers(5,10))
'''
#@staticmethod
class dates:
    def __init__(self,date):
        self.date=date
    
    def getDate(self):
        return self.date
    @staticmethod
    def toDashDate(date):
        return date.replace("/","-")

date=dates("10-10-2019")
datefromDB=("10/10/2019")
datewithDash=dates.toDashDate(datefromDB)
if (date.getDate()==datewithDash):
    print("Equal")
else:
    print("Unequal")




    