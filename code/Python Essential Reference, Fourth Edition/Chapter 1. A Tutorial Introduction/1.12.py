#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.12 Generators

def countdown(n):
    print("Counting down!")
    while n > 0:
        yield n # Generate a value (n)
        n -= 1

c = countdown(5)
print(c)
print(c.__next__()) # 5
print(c.__next__()) # 4
print(c.__next__()) # 3

for i in countdown(5):
    print(i,end=' ')
print()

# tail a file (like tail -f)
import time
def tail(f):
    f.seek(0,2)     # Move to EOF
    while True:
        line = f.readline()     # Try reading a new line of text
        if not line:
            time.sleep(0.1)
            continue
        yield line

def grep(lines, searchtext):
    for line in lines:
        if searchtext in line: yield line

# A python implement of Unix "tail -f | grep python"
wwwlog = tail(open("access-log"))
pylines = grep(wwwlog,"python")
for line in pylines:
    print(line,end='')
