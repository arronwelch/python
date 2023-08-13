#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.10 Iteration and Looping

print("the 1st way:")
for n in [1,2,3,4,5,6,7,8,9]:
    print("2 to the %d power is %d" % (n, 2**n))
print('')

print("the 2nd way:")
for n in range(1,10):
    print("2 to the %d power is %d" % (n, 2**n))
print()

# range(i, j, [,stride]) function : with values i to j-1
# If the starting value is omitted, it's taken to be zero.
# An optional stride can also be given as a third argument.

a = range(5)        # a = 0,1,2,3,4
print("a = ", end='')
for n in a:
    print("%d" % (n), end=' ')
print()

b = range(1,8)      # b = 1,2,3,4,5,6,7
print("b = ", end='')
for n in b:
    print("%d" % (n), end=' ')
print()

c = range(0,14,3)   # c = 0,3,6,9,12
print("c = ", end='')
for n in c:
    print("%d" % (n), end=' ')
print()

d = range(8,1,-1)   # d = 8,7,6,5,4,3,2
print("d = ", end='')
for n in d:
    print("%d" % (n), end=' ')
print()

sum = 0
#LargeRange = 100000000
LargeRange = 10000
for i in range(LargeRange):  # i = 0,1,2,...,99999999
    sum += i
print("0+1+2+...+99999999 = %d" % (sum))
# In Python3, the xrange() function has been renamed to range()
# and the functionality of the old range() function has been removed.

# strings
a = "Hello World"
# Print out the individual characters in a
print("a = ", end='')
for c in a:
    print(c,end=' ')
print()

# lists
b = ["Dave","Mark","Ann","Phil"]
# Print out the members of a list
print("b = ",end='')
for name in b:
    print(name,end=' ')
print()

# dictionaries
c = { 'GOOD' : 490.10, 'IBM' : 91.50, 'AAPL' : 123.15 }
# Print out of the members of a dictionary
print("c = ",end='')
for key in c:
    print(key,end=':')
    print(c[key],end=' ')
print()

# files
# Print all of the lines in a file
f = open("foo.txt")
index = 0
print("f = ")
for line in f:
    print("index.%02d:" % (index),end='')
    print(line,end='')
    index+=1
print()
