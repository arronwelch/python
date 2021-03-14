#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*arg,**kw):
        print('call %s():' % func.__name__)
        return func(*arg,**kw)
    return wrapper

@log
def now():
    print('2021-03-14')

print(now())

def log_arg(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*arg,**kw)
        return wrapper
    return decorator

@log_arg('execute')
def now_arg():
    print('2021-03-14')

print(now_arg())



# Exercise:
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time

def metric(fn):
    print('%s executed in %s ms' % (fn.__name__, 10.24))
    return fn

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')