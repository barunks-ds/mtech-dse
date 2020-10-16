# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:37:46 2020

@author: Riddhi
"""

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Bst(object):
    def __init__(self):
        self.root = None
    def insert(self, value):
        node = Node(value)
        if self.root == None:
            self.root = node
            return
        temp = self.root
        while True:
            if temp.value > node.value:
                if temp.left == None:
                    temp.left = node
                    break
                else:
                    temp = temp.left
            else:
                if temp.right == None:
                    temp.right = node
                    break
                else:
                    temp = temp.right
    
    def preorderRecursive(self, node, lst):
        if node == None:
            return
        lst.append(node.value)
        self.preorderRecursive(node.left, lst)
        self.preorderRecursive(node.right, lst)

    def preOrder(self):
        lst = []
        if self.root == None:
            return lst
        else:
            self.preorderRecursive(self.root, lst)
        return lst

    def postorderRecursive(self, node, lst):
        if node == None:
            return
        self.postorderRecursive(node.left, lst)
        self.postorderRecursive(node.right, lst)
        lst.append(node.value)

    def postOrder(self):
        lst = []
        if self.root == None:
            return lst
        else:
            self.postorderRecursive(self.root, lst)
        return lst
        
    def inorderRecursive(self, node, lst):
        if node == None:
            return
        self.inorderRecursive(node.left, lst)
        lst.append(node.value)
        self.inorderRecursive(node.right, lst)
                
    def inOrder(self):
        lst = []
        if self.root == None:
            return lst
        else:
            self.inorderRecursive(self.root, lst)
        return lst

import random        
tree = Bst()
for i in range(0,10):
    tree.insert(random.randint(1,30))

print("\nPreorder: ",tree.preOrder())
print("\nInorder: ",tree.inOrder())
print("\nPostorder: ",tree.postOrder())
