#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# a Higher-order function:
def add(x,y,f):
    return(f(x)+f(y))

# TEST

print(add(1,-2,abs))
if add(1,-2,abs) == 3:
    print('Test Pass!')
else:
    print('Test Fail!')


# map():
def f(x):
    return x*x

r = map(f,[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

s = list(map(str,range(10)))
print(s)

# reduce
from functools import reduce
def add(x,y):
    return(x+y)

print(reduce(add,[1,3,5,7,9]))

# list [1,3,5,7,9] to int 13579
def fn(x,y):
    return(x*10+y)

print(reduce(fn,[1,3,5,7,9]))

def char2num(s):
    num_s = list(map(str,range(10)))
    num_i = list(range(10))
    digits = dict(zip(num_s,num_i))
    return digits[s]

print(reduce(fn,map(char2num,'13579')))

def str2int(s):
    return(reduce(fn,map(char2num,s)))

print(str2int('13579'))

def str2int_a(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))

print(str2int_a('123456'))

# ambda函数也叫匿名函数 
# 它允许快速定义单行函数，类似于C语言的宏
# lambda [arg1 [, agr2,.....argn]] : expression
g = lambda x : x ** 2
print(g(3))

g = lambda x,y,z : (x+y)**z
print(g(1,2,2))


def normalize(name):
    return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    return reduce(lambda x,y:x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

