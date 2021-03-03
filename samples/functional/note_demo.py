#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])    
print(list(r))


print('-----------------')

L =[]
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)

print('-----------------')

from functools import reduce

def add(x,y):
    return x+y

r = reduce(add,[1,3,5,7,9])
print(r)

if r == (1+3+5+7+9):
    print('Test Pass!')
else:
    print('Test Fail!')

print('-----------------')

def fn(x,y):
    return x*10+y

r = reduce(fn,[1,3,5,7,9]) 
print(r)

print('-----------------')

def char2num(s):
    digits = {
        '0': 0,
        '1': 1, 
        '2': 2, 
        '3': 3, 
        '4': 4, 
        '5': 5, 
        '6': 6, 
        '7': 7, 
        '8': 8, 
        '9': 9
        }
    return digits[s]

print(reduce(fn,map(char2num,'13579')))

