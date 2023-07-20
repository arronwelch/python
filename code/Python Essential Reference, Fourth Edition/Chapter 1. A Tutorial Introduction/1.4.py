#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Input and Output

# $ echo "the first line" > foo.txt
# $ echo "the second line" >> foo.txt
# python3 1.4.py
f = open("foo.txt")     # Returns a file object
line = f.readline()     # Invokes readline() method on file
while line:
    # print line,       # trailing ',' omits newline character
    print(line,end='')  # Use in Python 3
    line = f.readline()
f.close

# Python provides a dedicated statement: for
for line in open("foo.txt"):
    print(line,end='')

principal = 1000    # Initial amount
rate = 0.05         # Interest rate
numyears = 5        # Number of years
year = 1
f = open("out1", "w")    # Open a file for writing
while year <= numyears:
    principal = principal * (1 + rate)
    #print >>f, "%3d %0.2f" % (year,principal)
    print("%3d %0.2f" % (year,principal), file=f)
    year += 1
f.close()

principal = 1000    # Initial amount
rate = 0.05         # Interest rate
numyears = 5        # Number of years
year = 1
f = open("out2", "w")    # Open a file for writing
while year <= numyears:
    principal = principal * (1 + rate)
    #print >>f, "%3d %0.2f" % (year,principal)
    f.write("%3d %0.2f\n" % (year,principal))
    year += 1
f.close()

import sys
sys.stdout.write("\nEnter your name :") # need '\n' to flush system streams
name = sys.stdin.readline() # name with '\n'
print("Hello,%s" % name, end='\n')

# name = raw_input("Enter your name :") # Python2
name = input("Enter your name :") # name without '\n' # Python3
print("Hello,%s" % name, end='\n') # print show NO '%'
