# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:41:26 2020

@author: Riddhi

Desc: Only change in recursion_one and recursion_two is print statement
      position changed, and the out is in reversed. Analyze find the reason
      of reversed output
"""


def recursion_one(value):
    if(value < 0):
        return
    print(value, end='\n')
    recursion_one( value -1 )

def recursion_two(value):
    if(value < 0):
        return
    recursion_two(value - 1)
    print(value, end='\n')
    
print("Calling recursion_one")
recursion_one(5)
print("Calling recursion_two")
recursion_two(5)


