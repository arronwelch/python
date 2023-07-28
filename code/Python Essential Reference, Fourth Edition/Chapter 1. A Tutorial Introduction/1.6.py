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
