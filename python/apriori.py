# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 18:31:14 2020

@author: Riddhi
"""

import sys
import numpy as np
import pandas as pd
from apyori import apriori

file = pd.read_excel("../data/data1.xlsx")
print(file.head())
data = file[['InvoiceNo','Description']].copy()
group_data = data.groupby('InvoiceNo')
group_data.fillna(0,inplace=True)
record_set = []
for inv, g in group_data:
    lst = g['Description'].values.tolist()
    record_set.append(lst)
print(record_set)

frq_items = apriori(record_set, min_support = 0.003,
                    min_confidence = 0.20,
                    min_lift=3,min_length=2) 
results = list(frq_items)
print(results.head())

