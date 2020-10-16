# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 00:44:09 2020

@author: Riddhi
"""


from nsetools import Nse
nse = Nse()
print (nse)
q = nse.get_quote('infy')
from pprint import pprint
pprint(q)
