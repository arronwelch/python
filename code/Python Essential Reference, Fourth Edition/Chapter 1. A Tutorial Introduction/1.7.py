#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.7 Tuples

first_name = "Bob"
last_name = "Bill"
phone = 111222

# stock = ('GOOG', 100, 490.10)
# address = ('www.python.org', 80)
# person = (first_name, last_name, phone)

stock = 'GOOG', 100, 490.10
address = 'www.python.org', 80
person = first_name, last_name, phone

print(stock)
print(address)
print(person)

item = "item"
a = ()      # 0-tuple (empty tuple)
b = (item,) # 1-tuple (note that trailing comma)
c = item,   # 1-tuple (note that trailing comma)

print(a)
print(b)
print(c)
