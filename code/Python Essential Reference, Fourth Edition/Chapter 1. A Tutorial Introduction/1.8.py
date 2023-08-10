#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.8 Sets

s = set([3,5,9,10])     # Create a set of numbers
t = set("Hello")        # Create a set of unique characters
print(s)
print(t)

a = t | s   # Union of t and s
b = t & s   # Intersection of t and s
c = t - s   # Set difference (items in t, but not in s)
d = t ^ s   # Symmetric difference (items in t or s, but not both)

print(a)
print(b)
print(c)
print(d)

t.add('x')              # Add a single item
s.update([10,37,42])    # Adds multiple items to s

print(t)
print(s)

t.remove('H')
print(t)
