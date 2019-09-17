#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 14:32:02 2017

@author: shubham

++++++++++++++++++++++++CLASS BASED+++++++++++++++++++++++
"""

class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
if __name__=="__main__":
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))

    obj=cal(a,b)

    obj.add()
    obj.sub()
    obj.mul()
    round(obj.div(),2)



'''++++++++++++++++++++Normal Function Based +++++++++++++++++'''

# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y


