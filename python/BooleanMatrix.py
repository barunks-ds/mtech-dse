# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:24:22 2020

@author: Riddhi
Usage: 
    mat = BooleanMatrix([[0, 0, 1], [1, 0, 0], [1, 1, 0]])
    print(mat)
    b2 = mat.dot(mat)
    print(b2)
    b3 = b2.dot(mat)
    print(b3)
    b4 = b3.dot(mat)
    print(b4)

    a = BooleanMatrix([[0, 1, 1], [0, 0, 1], [0, 0, 0]])
    print(a)
    b = BooleanMatrix([[0, 0, 0], [1, 0, 0], [1, 1, 0]])
    print(b)
    aor = a | b
    print(aor)
    aand = a & b
    print(aand)
    anot = ~aand
    print(anot)

"""
import numpy as np
import random
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
            raise ValueError("incorrect parameters passed:"+str(len(args)))
        
        
    def dot(self, b):
        if self.mCols < b.mRows:
            raise ValueError("dot product can not generated")
        temp = BooleanMatrix(self.mRows, b.mCols)
        for i in range(self.mRows):
            for j in range(self.mCols):
                for k in range(self.mCols):
                    temp.mMatrix[i][j] = temp.mMatrix[i][j] | (self.mMatrix[i][k] & b.mMatrix[k][j])
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
        
    def __getitem__(self, key):
        return self.mMatrix[key]
    
    def __eq__(self, b):
        if ((self.mCols != b.mCols) or (self.mRows != b.mRows)):
            return False
        for i in range(self.mRows):
            for j in range(self.mCols):
                if(self.mMatrix[i][j] != b.mMatrix[i][j]):
                    return False
        return True
    
    def __ne__(self, b):
        if ((self.mCols != b.mCols) or (self.mRows != b.mRows)):
            return True
        for i in range(self.mRows):
            for j in range(self.mCols):
                if(self.mMatrix[i][j] != b.mMatrix[i][j]):
                    return True
        return False
    
    @staticmethod
    def generateDigraph(numVertices):
        vertices = numVertices
        min_edges = vertices - 1    
        max_edges = vertices * min_edges
        edges = int((min_edges + max_edges) / 2)
        mat = BooleanMatrix(numVertices, numVertices)
        ec = 0
        #print("Vertices:",vertices)
        #print("Edges:", edges)
        for i in range(edges):
            v1 = i % vertices #random.randint(1,vertices)
            v2 = random.randint(0,vertices*vertices) % vertices
            if v1 == v2:
                continue
            if mat[v1][v2] == False:
                ec += 1
                #print("Edge: ("+str(v1)+","+str(v2)+")")
                mat[v1][v2] = True
        #print("Edges:", ec)
        #print(mat)
        return mat
    