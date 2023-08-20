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

