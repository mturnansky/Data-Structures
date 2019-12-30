#linked list

#requires node object
from node import Node

class UnorderedList:
    
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def search(self,item):
        current = self.head
        found = False
        
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
                
        return found
    
    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        
    def size(self):
        count = 0
        current = self.head
        
        while current != None:
            current = current.get_next()
            count += 1
        
        return count
        
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        
        
    def index(self,item):
        current = self.head
        count = 0
        
        while current != item:
            if current.get_data() == None:
                raise KeyError
            
            current = current.get_next()
            count += 1
        
        return count
    
    def pop(self):
        current = self.head
        previous = None
        while current != None:
                previous = current
                current = current.get_next()
        
        previous.set_next(None)
        return current
    
    def append(self, item):
        current = self.head
        while current != None:
                current = current.get_next()
        
        item = Node(item)
        current.set_next(item)
        
        
            
        