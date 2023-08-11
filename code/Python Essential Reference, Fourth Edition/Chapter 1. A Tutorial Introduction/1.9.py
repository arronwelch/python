#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.9 Dictionaries

stock = {
    "name"  :   "GOOD",
    "shares":   100,
    "price" :   490.10
    }

name = stock["name"]
value = stock["shares"] * stock["price"]

print("name = %s" % name)
print("value = %f" % value)

stock["shares"] = 75            # modifying objects
stock["date"] = "June 7, 2007"  # inserting objects

print("stock = ")
print(stock)
