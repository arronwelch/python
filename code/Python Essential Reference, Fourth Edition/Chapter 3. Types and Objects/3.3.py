#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 3.3 Reference Counting and Garbage Collection

# All objects are reference-counted.
# An object's reference count is increased whenever it's
# assigned to a new name or placed in a container such as a list, tuple, or dictionary,as
# show here:

import sys

a = 37      # Creates an object with value 37
print('sys.getrefcount(a) = ', sys.getrefcount(a)) # it's 14? not 1?
print('id(a) \t\t= ', id(a))
b = a       # Increases reference count on 37
print('sys.getrefcount(a) = ', sys.getrefcount(a))
print('id(b) \t\t= ', id(b))
c = []
c.append(b) # Increases reference count on 37
print('sys.getrefcount(a) = ', sys.getrefcount(a))
print('id(c[0]) \t= ', id(c[0]))

del a       # Decrease reference count of 37
b = 42      # Decrease reference count of 37
print('sys.getrefcount(b) = ', sys.getrefcount(b))
print('id(b) \t\t= ', id(b))
c[0] = 2.0  # Decrease reference count of 37
print('sys.getrefcount(c[0]) = ', sys.getrefcount(c[0]))
print('id(c[0]) \t\t= ', id(c[0]))

# In many cases, the reference count is much higher than you might guess.
a = { }
b = { }
a['b'] = b  # a contains reference to b
b['a'] = a  # b contains reference to a
del a
del b

# resulting in a memory leak
# To address this problem, the interpreter periodically executes a cycle detector that
# searches for cycles of inaccessible objects and deletes them.
