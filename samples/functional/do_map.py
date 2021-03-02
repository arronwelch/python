#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def f(x):
    return x*x

s = list(map(f,[x for x in range(10) if x > 0]))

print(s)


# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# TEST
if s == [1, 4, 9, 16, 25, 36, 49, 64, 81]:
    print('Test Pass!')
else:
    print('Test Fail!')
