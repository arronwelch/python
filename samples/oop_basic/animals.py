#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 继承和多态
# Subclass Base class Super class

class Animals(object):
    def run(self):
        print('Animal is running...')

A1 = Animals()

A1.run()

class Dog(Animals):
    pass

class Cat(Animals):
    pass

D1 = Dog()
D1.run()

C1 = Cat()
C1.run()

class Dog(Animals):
    def run(self):#多态
        print('Dog is running...')
    def eat(self):
        print('Dog eatting meat...')

class Cat(Animals):
    def run(self):
        print('Cat is running...')

D1 = Dog()
D1.run()

C1 = Cat()
C1.run()

a = Animals()
d = Dog()
c = Cat()

def run_twice(a):
    a.fun()
    a.fun()

class Tortoise(object):
    def fun(self):
        print('T is running ...')

bb = Tortoise()

bb.fun()

run_twice(bb)