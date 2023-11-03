#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 3.8 Sequence Types:Lists

# list(s) | Converts s to a list.
s = 'abcd'
print('s =',s,type(s))
l = list(s)
print('l =',l,type(l))

# s.append(x) | Appends a new element,x,to the end of s.
l.append('e')
print('l =',l,type(l))

# s.extend(t) | Appends a new list,t,to the end of s.
l.extend(list('fg'))
l.extend('hi')
print('l =',l,type(l))

# s.count(x) | Counts occurrences of x in s.
print('l.count(\'i\')=',l.count('i'))
print('l.count(\'j\')=',l.count('j'))
