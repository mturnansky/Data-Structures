# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 09:24:14 2019

@author: Mat
"""
#ADT ordered list (increasing order)

from node import Node

class OrderedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        count = 0
        current = self.head
        
        while current != None:
            current = current.get_next()
            count += 1
        
        return count

#find item via a linked list structure
    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

#add item to list while maintaining order 
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
                
        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
            
#return the index of the item
    def index(self,item):
        current = self.head
        count = 0
        
        while current != item:
            if current.get_data() > item:
                raise KeyError
            
            current = current.get_next()
            count += 1
        
        return count
#remove and return element at position args
    def pop(self, *args):
        if args != None:
            pos = self.size()
        
        else:
            pos = args
        
        current = self.head
        previous = None
        count = 0 
        
        while count < pos:
            count += 1
            previous = current
            current = current.get_next()
        
        previous.set_next(current.get_next())
        return current
    
        
        
        
            
            
    
