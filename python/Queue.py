# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:56:36 2020

@author: Riddhi

What is Queue?
Queue is a linear data structure where the first element is inserted from one end called REAR and deleted from the other end called as FRONT.

Front points to the beginning of the queue and Rear points to the end of the queue.

Queue follows the FIFO (First - In - First Out) structure.

According to its FIFO structure, element inserted first will also be removed first.

In a queue, one end is always used to insert data (enqueue) and the other is used to delete data (dequeue), because queue is open at both its ends.

The enqueue() and dequeue() are two important functions used in a queue.
"""


class MyQueue:
    
    def __init__(self):
        self.data = []
        
    def enqueue(self, val):
        self.data.append(val)
    
    def dequeue(self):
        val = self.data.pop(0)
        return val
    
    def printQueue(self):
        if(len(self.data) <= 0):
            print("Queue is empty")
            return
        for i in self.data[::]:
            print(i,end=" ")
        