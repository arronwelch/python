#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2.8 Decorators

# class Foo(object):
#     @staticmethod
#     def bar():
#         pass
#     @foo
#     @bar
#     def spam():
#         pass

# More information about decorators can be found in Chapter 6,
# "Functions and Functional Programming", and Chapter 7,"Classes and
# Object-Oriented Programming".

def log_function(func):
    def wrapper(*args,**kwargs):
        print("Calling function {} with arguments {}".format(func.__name__,args))
        result = func(*args,**kwargs)
        print("Function {} returned {}".format(func.__name__,result))
        return result
    return wrapper

@log_function
def my_function(arg1, arg2):
    return arg1+arg2

my_function(1, 2)

@log_function
def my_function_x(arg1, arg2, arg3):
    return arg1+arg2+arg3

my_function_x(1,2,3)
