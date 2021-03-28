#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student1(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self,name):
        if isinstance(name,str):
            self.__name = name
        else:
            raise ValueError('bad name')
    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad socre')


class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender = gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')