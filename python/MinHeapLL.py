# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 20:35:23 2020

@author: Riddhi
"""

import copy

class Queue (object):
    def __init__(self):
        self.q = []
    def enqueue(self, val):
        self.q.append(val)
    def dequeue(self):
        if len(self.q) > 0:
            obj = self.q[0]
            self.q = self.q[1:]
            return obj
        return None
    def empty(self):
        return len(self.q) == 0

class HeapNode(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None
    def __str__(self):
        return str(self.value)

class MinHeapLL(object):
    
    def __init__(self):
        self.root = None

    def findLastNode(self):
        lastNode = self.root
        
        if self.root != None:
            q = Queue()
            q.enqueue(self.root)
            while not q.empty():
                temp = q.dequeue()
                if temp != None:
                    lastNode = temp
                    if temp.left != None:
                        q.enqueue(temp.left)
                    if temp.right != None:
                        q.enqueue(temp.right)
        return lastNode
    
    def heapify(self, node):
        if node == None or node.parent == None:
            return
        if node.value < node.parent.value:
            (node.value, node.parent.value) = (node.parent.value, node.value)
            self.heapify(node.parent)
            
    def insert(self, value):
        node = HeapNode(value)
        if self.root == None:
            self.root = node
            return
        q = Queue()
        q.enqueue(self.root)
        while not q.empty():
            temp = q.dequeue()
            if temp.left == None:
                temp.left = node
                node.parent = temp
                break
            elif temp.right == None:
                temp.right = node
                node.parent = temp
                break
            else:
                q.enqueue(temp.left)
                q.enqueue(temp.right)
        self.heapify(node)
                
    def heapifyTopToBottom(self, node):
        if node == None:
            return
        if node.left != None and node.right != None:
            if node.left.value < node.right.value:
                (node.value, node.left.value) = (node.left.value, node.value)
                self.heapifyTopToBottom(node.left)
            else:
                (node.value, node.right.value) = (node.right.value, node.value)
                self.heapifyTopToBottom(node.right)
        elif node.left != None:
            if node.left.value < node.value:
                (node.value,node.left.value) = (node.left.value, node.value)
                self.heapifyTopToBottom(node.left)


    def delete(self):
        deleted = copy.deepcopy(self.root)
        if deleted == None:
            return deleted
        if self.root.left == None and self.root.right == None:
            self.root = None
            return deleted
        lastNode = self.findLastNode()
        print("Last node: "+str(lastNode))
        if lastNode != None:
            if lastNode.parent.left == lastNode:
                lastNode.parent.left = None
            else:
                lastNode.parent.right = None
            lastNode.Parent = None
            self.root.value = lastNode.value
            self.heapifyTopToBottom(self.root)
        return deleted
    
    def __str__(self):
        lst = []
        
        q = Queue()
        q.enqueue(self.root)
        while True:
            if len(q.q) <= 0:
                break
            t = q.dequeue()
            if t != None:
                lst.append(t.value)
                q.enqueue(t.left)
                q.enqueue(t.right)
        return str(lst)                   

H = MinHeapLL()

H.insert(10)
H.insert(6)
H.insert(5)
#H.insert(4)

print(H)
d = H.delete()
print("Deleting: ",d,end = "\n")
print(H)
d = H.delete()
print ("Deleting: ",d, end="\n")
print(H)
d = H.delete()
print ("Deleting: ",d, end="\n")
print(H)
d = H.delete()
print ("Deleting: ",d, end="\n")
print(H)
d = H.delete()
print ("Deleting: ",d, end="\n")
print(H)
d = H.delete()
print ("Deleting: ",d, end="\n")
print(H)
d = H.delete()
print ("Deleting: ",d, end="\n")
print(H)
d = H.delete()
print ("Deleting: ",d, end="\n")
print(H)
d = H.delete()
print ("Deleting: ",d, end="\n")
print(H)