# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 11:00:40 2019

@author: Mat
"""

#queue where rear is back 
class Queue:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        item = self.items[0]
        self.items = self.items[1:]
        return item
    def size(self):
        return len(self.items)
    
