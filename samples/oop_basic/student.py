#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Object Oriented Programming (OOP)
# 一种程序设计思想
# Class
# Property
# Method

# dict
std1 = {'name':'Michael','score':98}
std2 = {'name':'Bob','score':81}

def print_score(std):
    print('%s:%s' % (std['name'],std['score']))

print_score(std1)
print_score(std2)

# print('%s' % std1)

class Student(object):

    def __init__(self,name,score):
        self.name = name
        self.score = score
    
    def print_score(self):
        print('%s:%s' % (self.name,self.score))

bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()

# Instance
