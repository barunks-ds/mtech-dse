

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:07:02 2020

@author: Riddhi
"""


def is_palindrom_barun(word):
    #print(word)
    if(len(word) <= 1):
        #print(word[1:-1])
        return True
    if(word[0] == word[-1]):
        return is_palindrom_barun(word[1:-1])
    else:
        return False
    
def is_palindrom_dheeraj(word):
    if(word == word[::-1]):
        return True
    return False

def rev_str(string1):
    return string1[::-1]

def is_palindrom_swathi(word):
    rev = rev_str(word)
    if(word == rev):
        return True
    return False

    
    
    

    




# =============================================================================
# def test_func(*param2, *param2):
#     print(type(param2))
# test_func()
# =============================================================================
