#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Student(object):
#     def get_score(self):
#         return self._score
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integar!')
#         if value < 0 or value > 100:
#             raise ValueError('score must betweeen 0~100!')
#         self._score = value
# 
# 
# class Student(object):
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('score must be an integar!')
#         if value < 0 or value > 100:
#             raise ValueError('score must betweeen 0~100!')
#         self._score = value
# 
# class Student(object):
#     @property
#     def birth(self):
#         return self._birth
#     @birth.setter
#     def birth(self,value):
#         self._birth = value
#     @property
#     def age(self):
#         return 2021-self._birth

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')