#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.11 Functions

def remainder(a,b):
    q = a // b      # // is truncating division.
    r = a - q*b
    return r

result = remainder(37,15)
print("37 remainder by 15 is %d" % (result))

def divide(a,b):
    q = a // b      # If a and b are integers, q is integer
    r = a - q*b
    return (q,r)

quotient, remainder = divide(1456,33)
print("1456 / 33 = %d --- %d" %(quotient,remainder))

def connect(hostname,port,timeout=300):
    PASS # Function body
    print("Function body: timeout=%d" % timeout)
