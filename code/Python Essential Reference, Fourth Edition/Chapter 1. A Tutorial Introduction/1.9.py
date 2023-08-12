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

prices = {
    "GOOD"  : 490.10,
    "AAPL"  : 123.50,
    "IBM"   : 91.50,
    "MSFT"  : 52.13
}

print("stock prices = ")
print(prices)

prices = {}     # An empty dict
print("prices is An empty dict:")
print(prices)
prices = dict() # An empty dict
print("prices is An empty dict:")
print(prices)

if "SCOX" in prices:
    p = prices["SCOX"]
else:
    p = 0.0
print("p = %f" % p)

p = prices.get("SCOX",0.0)
print("p = %f" % p)

prices = {
    "GOOD"  : 490.10,
    "AAPL"  : 123.50,
    "IBM"   : 91.50,
    "MSFT"  : 52.13
}
# To obtain a list of dictionary keys, convert a dictionary to a list:
syms = list(prices)     # syms = ["AAPL", "MSFT", "IBM", "GOOD"]
print("syms =")
print(syms)

del prices["MSFT"]
print("stock prices = ")
print(prices)
