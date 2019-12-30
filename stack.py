# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:03:20 2019

@author: Mat
"""

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def rev_string(string):
    m = Stack()
    n = Stack()
    for element in string:
        m.push(element)
    while not m.is_empty():
        n.push(m.pop())
    return n

string = "cat"

rev = rev_string(string)
rev.pop()

print(rev.pop())
    