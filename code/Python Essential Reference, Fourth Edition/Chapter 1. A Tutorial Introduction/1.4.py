#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Input and Output

# $ echo "the first line" > foo.txt
# $ echo "the second line" >> foo.txt
# python3 1.4.py
f = open("foo.txt") # Returns a file object
line = f.readline() # Invokes readline() method on file
while line:
    # print line,      # trailing ',' omits newline character
    print(line,end='') # Use in Python 3
    line = f.readline()
f.close
