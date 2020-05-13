# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:49:19 2020

@author: Riddhi
"""


import matplotlib.pyplot as plt
import csv

x=[]
y=[]

with open('D:/Projects/PythonPractice/csvfile1.txt', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))


plt.plot(x,y, marker='o')

plt.title('Data from the CSV File: People and Expenses')

plt.xlabel('Number of People')
plt.ylabel('Expenses')

plt.show()