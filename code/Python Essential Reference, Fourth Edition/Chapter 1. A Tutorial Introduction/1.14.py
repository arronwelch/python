#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.14 Objects and Classes

items = [37, 42]    # Create a list object
print("items = ", items)
items.append(73)    # Call the append() method
print("items = ", items)
print(items.__dir__())
print(items.__add__([73,101])) # return the add result, not change objects oneself
items = items + [73,101] # python3
print("items = ", items)

class Stack(object):
    def __init__(self):     # Initialize the stack
        self.stack = []
    def push(self,object):
        self.stack.append(object)
    def pop(self):
        return self.stack.pop()
    def length(self):
        return len(self.stack)

s = Stack()     # Create a stack
s.push("Dave")  # Push some things onto it
s.push(42)
s.push([3,4,5])
x = s.pop()     # x gets [3,4,5]
print("x = ",x)
y = s.pop()     # y gets 42
print("y = ",y)
del s           # Destroy s

class Stack1(list):
    # Add push() method for stack interface
    # Note: lists already provide a pop() method.
    def push(self,object):
        self.append(object)

s = Stack1()     # Create a stack
s.push("Dave")  # Push some things onto it
s.push(42)
s.push([3,4,5])
x = s.pop()     # x gets [3,4,5]
print("x = ",x)
y = s.pop()     # y gets 42
print("y = ",y)
del s           # Destroy s

class EventHandler(object):
    @staticmethod
    def dispatcherThread():
        while (1):
            # Wait for requests
            pass

EventHandler.dispatcherThread()     # Call method like a function
