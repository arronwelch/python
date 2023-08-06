#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.7 Tuples

first_name = "Robert"
last_name = "Smith"
phone = 123456

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

name, shares, price = stock
print(name)
print(shares)
print(price)

host, port = address
print(host)
print(port)

first_name1, last_name1, phone1 = person
print(first_name1)
print(last_name1)
print(phone1)

# File containing lines of the form "name,shares,price"
filename = "portfolio.csv"
portfolio = []
for line in open(filename):
    fields = line.split(",")    # Split each line into a list
    name = fields[0]            # Extract and convert individual fields
    shares = int(fields[1])
    price = float(fields[2])
    stock = (name,shares,price) # Create a tuple (name, shares, price)
    portfolio.append(stock)     # Append to list of records
    print(portfolio)

