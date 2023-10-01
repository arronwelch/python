#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 3.5 First-Class Objects

items = {
    'number' : 42,
    'text' : "Hello World"
}

print('items = ', items)

items["func"] = abs         # Add the abs() function
print('items = ', items)

import math
items["mod"] = math         # Add a module
print('items = ', items)

items["error"] = ValueError # Add an exception type
print('items = ', items)

nums = [1,2,3,4]
items["append"] = nums.append # Add a method of another object
print('items = ', items)

print('items["func"](-45) = ',items["func"](-45)) # Executes abs(-45)

print('items["mod"].sqrt(4) = ',items["mod"].sqrt(4)) # Executes math.sqrt(4)

try:
    x = int("a lot")
except items["error"] as e: # Same as "except ValueError as e"
    print("Couldn't convert")

items["append"](100)    # Executes nums.append(100)
print('nums = ',nums)

line = "GOOG,100,490.10"
# print('line = ',line)
field_types = [str, int, float]
raw_fields = line.split(',')
# print('raw_fileds = ',raw_fields)
fields = [ty(val) for ty,val in zip(field_types, raw_fields)]
print('fields = ',fields)
