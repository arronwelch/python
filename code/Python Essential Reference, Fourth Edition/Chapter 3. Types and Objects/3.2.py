#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 3.2 Object Identity and Type

# the built-in function id() returns the identity of an object as an integer.
a = 1
print('id(a) = ',id(a))

# The is operator compares the identity of two objects.
# The built-in function type() returns the type of an object.

# Compare two objects
def compare(a, b):
    if a is b:
        # a and b are the same object
        # statement
        print('a and b are the same object')
    if a == b:
        # a and b have the same value
        # statement
        print('a and b have the same value')
    if type(a) is type(b):
        # a and b have the same type
        # statement
        print('a and b have the same type')

b = 2
compare(a, b)

# All type objects are assigned names that can be used to perform type checking.
s = [1, 2, 3]
item = 4
print('s = ', s)
if type(s) is list:
    s.append(item)
print('s = ', s)

d = {
    "name" : "GOOG",
    "shares" : 100,
    "price" : 490.10,
}

t = { "count" : 1000 }

print('d = ', d)
if type(d) is dict:
    d.update(t)
print('d = ', d)

item = 5
if isinstance(s, list):
    s.append(item)
print('s = ', s)

t = { "percent" : 0.04 }
if isinstance(d, dict):
    d.update(t)
print('d = ', d)
# Because the isinstance() function is aware of inheritence, it is the preferred way to
# check the type of any Python object.

