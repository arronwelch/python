#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.6 Lists

names = [ "Dave", "Mark", "Ann", "Phil" ]

a = names[2]    # Returns the third item of the list, "Ann"
print("a = %s" % a)

print(names)
names[0] = "Jeff"   # Changes the first item to "Jeff"
print(names)

names.append("Paula")
print(names)

names.insert(2, "Thomas")
print(names)

b = names[0:2]  # Returns [ "Jeff", "Mark" ]
print(b)

c = names[2:]   # Returns [ "Thomas", "Ann", "Phil", "Paula" ]
print(c)

names[1] = 'Jeff'   # Replace the 2nd item in names with 'Jeff'
print(names)

names[0:2] = ['Dave', 'Mark', 'Jeff']   # Replace the first two items of
                                        # the list with the list on the right.
print(names)

a = [1,2,3] + [4,5]     # Result is [1,2,3,4,5]
print(a)

names = []      # An empty list
print(names)
names = list()  # An empty list
print(names)

a = [1, "Dave", 3.14, ["Mark", 7, 9, [100, 101]], 10]

print(a[1])         # Returns "Dave"
print(a[3][2])      # Returns 9
print(a[3][3][1])   # Returns 101
