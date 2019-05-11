# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:07:21 2019

@author: Aarav
"""

class calculator:
    a=5
    b=10
    def __init__(self):
        self.a=10
        self.b=20
    def addition(self):
        return self.a+self.b
    
    def subtraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a*self.b
    
    def divison(self):
        try:
            return self.a/self.b
        except:
            print("Exception occured")
            
    def all(self):
        add=self.a+self.b
        sub=self.a-self.b
        mul=self.a*self.b
        div=self.a/+self.b
        return add,sub,mul,div
    
    def printall(self):
        
        print("Arithematic opertion on the numbers: {0} {1}" .format(self.a,self.b))
        print("Addition  : {} " . format(self.addition()))
        print("Subtraction is :" + str(self.subtraction()))
        print("Multiplication is :" + str(self.multiplication()))
        print("Division is :" + str(self.divison()))
        print("Addition,subtraction,multiplication,division"+ str(self.all()))
       
            
        
c=calculator()
c.printall()

print(c.__module__)
print(__name__)

