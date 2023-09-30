#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 3.4 References and Copies

# immutable objects: numbers and strings
# mutable objects: lists and dictionaries

print('a and b refer to the same object:')
a = [1,2,3,4]
print('a = ', a)
print('id(a) = ', id(a))

b = a           # b is a reference to a
print('b = ', b)
print('id(b) = ', id(b))
print('b is a :', (b is a))

b[2] = -100     # Change an element in b
print('b[2] = ', b[2])
print('id(a) = ', id(a))
print('a = ', a)
print('id(b) = ', id(b))
print('b = ', b)
# Because a and b refer to the same object in this example

print('\na shallow copy:')
a = [ 1, 2, [3, 4] ]
b = list(a) # Create a shallow copy of a.
print('b is a :', (b is a))

b.append(100)   # Append element to b.
print('b = ', b)
print('a = ', a)

b[2][0] = -100  # Modify an element inside b
print('b[2][0] = ', b[2][0])
print('b = ', b)
print('a = ', a)    # Notice the change inside a

print('\na deep copy:')
import copy
a = [1, 2, [3, 4]]
print('a = ', a)
b = copy.deepcopy(a)
b[2][0] = -100
print('b = ', b)
print('a = ', a)    # Notice that a is unchanged
