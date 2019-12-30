# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:40:26 2019

@author: Mat
"""
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
    
    def set_next(self, new_next):
        self.next = new_next
       