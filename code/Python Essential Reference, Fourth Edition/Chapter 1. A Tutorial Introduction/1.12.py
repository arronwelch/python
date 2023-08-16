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
