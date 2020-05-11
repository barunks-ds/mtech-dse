# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:52:47 2020

@author: Riddhi
"""


#import array as ar
class MyStack:
    
    def __init__(self):
        self.data = []
        self.top = -1
    
    def pop(self):
        if(self.top >= 0):
            val = self.data[self.top]
            self.top = self.top - 1
            return val
        else:
            print("Stack is empty")
            
    def push(self, val):
        self.top = self.top+1
        self.data.insert(self.top,val)
    
    def printStack(self):
        if(self.top < 0):
            print("stack is emtpy")
            return
        for i in self.data[self.top::-1]:
            print(i, end = '\n')
            
ms = MyStack()
ms.push(2)
ms.push(3)
ms.push(4)
ms.push(5)
ms.printStack()
ms.pop()
ms.pop()
ms.pop()
ms.printStack()

            
        