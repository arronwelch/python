#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 3.6 Built-in Types for Representing Data

# 3.6.1 The None Type
s = "this is string"
if(isinstance(s, str)):
    print("\"",s,"\" is str Type")
else:
    print("\"",s,"\" is None Type")

n = None
if(isinstance(n, type)):
    print("\"",n,"\" is type")
else:
    print("\"",n,"\" not is type")

# 3.6.2.1 Numeric Types: Booleans
print(1 > 0)
print(-1 > 0)
a = -1
print('a = ', a)
a = 1 > 0
print('a = ', a)

# 3.6.2.2 Numeric Types: Integers
a = -2147483648
print('a = ',a,type(a))
b = 2147483647+1 # In Python3, the two types have been unified into a single integer type
print('b = ',b,type(b))
