# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:24:22 2020

@author: Riddhi
"""
import numpy as np

class BooleanMatrix(object):

    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            if isinstance(args[0], list):
                lst = args[0]
                self.mRows = len(lst)
                self.mCols = len(lst[0])
                self.mMatrix = np.array([[False]* self.mCols] * self.mRows, dtype=np.bool)
                for i in range(self.mRows):
                    for j in range(self.mCols):
                        self.mMatrix[i][j] = lst[i][j]
        elif len(args) == 2:
            self.mRows = args[0]
            self.mCols = args[1]
            self.mMatrix = np.array([[False]* self.mCols] * self.mRows, dtype=np.bool)
        else:
            raise ValueError("incorrect parameters passed:"+len(args))
        
        
    def dot(self, b):
        if self.mCols < b.mRows:
            raise ValueError("dot product can not generated")
        temp = BooleanMatrix(self.mRows, b.mCols)
        for i in range(self.mRows):
            for j in range(self.mCols):
                for k in range(self.mCols):
                    temp.mMatrix[i][j] = temp.mMatrix[i][j] | self.mMatrix[i][k] & b.mMatrix[k][j]
        return temp
    
    def __str__(self):
        string = "Matrix: Rows:"+str(self.mRows) + ", Cols:"+str(self.mCols)
#        string += " Rows:"+str(self.mRows)
#        string +="\nCols:"+str(self.mCols)
        for i in range(self.mRows):
            string +="\n["
            for j in range(self.mCols):
                string += (str(int(self.mMatrix[i][j])))+ " "
            string += "]"
        return string
            
                
    def __or__(self, b):
        if (self.mRows > b.mRows or
            self.mCols > b.mCols):
                raise ValueError("parameter 2 not correct")
        if not isinstance(b, BooleanMatrix):
            raise ValueError("parameter 2 not correct")
        temp = BooleanMatrix(self.mRows, self.mCols)
        for i in range(self.mRows):
            for j in range(self.mCols):
                temp.mMatrix[i][j] = self.mMatrix[i][j] | b.mMatrix[i][j]
        return temp
    
    def __and__(self, b):
        if (self.mRows > b.mRows or
            self.mCols > b.mCols):
                raise ValueError("parameter 2 not correct")
        if not isinstance(b, BooleanMatrix):
            raise ValueError("parameter 2 not correct")
        temp = BooleanMatrix(self.mRows, self.mCols)
        for i in range(self.mRows):
            for j in range(self.mCols):
                temp.mMatrix[i][j] = self.mMatrix[i][j] & b.mMatrix[i][j]
        return temp
 
    def __xor__(self, b):
        if (self.mRows > b.mRows or
            self.mCols > b.mCols):
                raise ValueError("parameter 2 not correct")
        if not isinstance(b, BooleanMatrix):
            raise ValueError("parameter 2 not correct")
        temp = BooleanMatrix(self.mRows, self.mCols)
        for i in range(self.mRows):
            for j in range(self.mCols):
                temp.mMatrix[i][j] = self.mMatrix[i][j] ^ b.mMatrix[i][j]
        return temp

    def __invert__(self):

        temp = BooleanMatrix(self.mRows, self.mCols)
        for i in range(self.mRows):
            for j in range(self.mCols):
                temp.mMatrix[i][j] = ~self.mMatrix[i][j]
        return temp
        