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
    pass    # Function body
    print("Function body: ")
    print("hostname=\"%s\"" % hostname,end=',')
    print("port=%d" % port,end=',')
    print("timeout=%d" % timeout)

connect('www.python.org',80)

connect(port=80,hostname='www.python.org')

count = 0   # a global variable
print("count=%d" % count)

def foo():
    global count
    count += 1  # Changes the global variable count

foo()
# After run foo(), print count value is 1
print("count=%d" % count)
