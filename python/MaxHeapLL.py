# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:50:31 2020

@author: Riddhi
"""
import copy

class QueueLL(object):
    def __init__(self):
        self.q = []
    
    def enqueue(self, node):
        self.q.append(node)

    def dequeue(self):
        if len (self.q) > 0:
            obj = self.q[0]
            self.q = self.q[1:]
            return obj
        return None
    
    def empty(self):
        return len (self.q) == 0

        
        

class HeapNode(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.value = val
    def __str__(self):
        return str(self.value)


class MaxHeapLL(object):

    def __init__(self):
        self.root = None
    
    def findLastNode(self):
        lastNode = None
        q = QueueLL()
        q.enqueue(self.root)
        while True:
            if q.empty():
                break
            temp = q.dequeue()
            if temp != None:
                if temp.left:
                    q.enqueue(temp.left)
                if temp.right:
                    q.enqueue(temp.right)
                lastNode = temp
        return lastNode

                
    def heapify(self, node):
        if node == None:
            return
        if node.parent == None:
            return
        if node.value > node.parent.value:
            temp = node.value
            node.value = node.parent.value
            node.parent.value = temp
            self.heapify(node.parent)
        
    def heapifyTopToBottom(self, node):
        if node == None:
            return
        if node.left != None and node.right != None:
            if node.left.value > node.right.value:
                temp = node.left.value
                node.left.value = node.value
                node.value = temp
                self.heapifyTopToBottom(node.left)
            else :
                temp = node.right.value
                node.right.value = node.value
                node.value = temp
                self.heapifyTopToBottom(node.right)
        elif node.left != None and node.left.value > node.value:
            temp = node.value
            node.value = node.left.value
            node.left.value = temp
            self.heapifyTopToBottom(node.left)


    def insertItem(self, val):
        if(self.root == None):
            self.root = HeapNode(val)
            return
        que = QueueLL()
        que.enqueue(self.root)
        newNode = None
        while True:
            temp = que.dequeue()
            if temp.left == None:
                newNode = HeapNode(val)
                temp.left = newNode
                newNode.parent = temp
                break
            elif temp.right == None:
                newNode = HeapNode(val)
                temp.right = newNode
                newNode.parent = temp
                break
            else:
                que.enqueue(temp.left)
                que.enqueue(temp.right)
        self.heapify(newNode)
        
    def deleteNode(self):
        temp = copy.deepcopy(self.root)
        if temp == None:
            return temp
        if self.root.left == None and self.root.right == None:
            self.root = None
            return temp
        
        succ = self.findLastNode()
        if succ.parent.left == succ:
            succ.parent.left = None
        else:
            succ.parent.right = None
        succ.parent = None
        
        self.root.value = succ.value
        self.heapifyTopToBottom(self.root)
        return temp

    def __str__(self):
        lst = []
        
        q = QueueLL()
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
    
H = MaxHeapLL()
H.insertItem(4)
H.insertItem(5)
H.insertItem(6)
H.insertItem(10)
print(H)
d = H.deleteNode()
print("Deleting: ",d,end = "\n")
print(H)
d = H.deleteNode()
print ("Deleting: ",d, end="\n")
print(H)
d = H.deleteNode()
print ("Deleting: ",d, end="\n")
print(H)
d = H.deleteNode()
print ("Deleting: ",d, end="\n")
print(H)
d = H.deleteNode()
print ("Deleting: ",d, end="\n")
print(H)
    