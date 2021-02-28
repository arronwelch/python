#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，
# 这种遍历我们称为迭代（Iteration）。

# 在Python中，迭代是通过for ... in来完成的，
# 而很多语言比如C语言，迭代list是通过下标完成的
# 只要是可迭代对象，无论有无下标，都可以迭代

d = {'a': 1, 'b': 2, 'c': 3} # this is a dict

for key in d:
    print(key)

# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
# 默认情况下，dict迭代的是key。
# 如果要迭代value，可以用for value in d.values()，
# 如果要同时迭代key和value，可以用for k, v in d.items()。

print('----------------')
print('value:')
print('----------------')
for value in d.values():
    print(value)

print('----------------')
print('key:value')
print('----------------')
for k,v in d.items():
    print(k,v)

# 由于字符串也是可迭代对象，因此，也可以作用于for循环：

for ch in 'ABC':
    print(ch)

from collections.abc import Iterable

isinstance('abc', Iterable) # str是否可迭代

isinstance([1,2,3], Iterable) # list是否可迭代

isinstance(123, Iterable) # 整数是否可迭代

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y,z in [(1, 1,2), (2, 4,6), (3, 9,8)]:
    print(x,y,z)



def findMinAndMax(L):
    if not L:
        return(None,None)
    Min = L[0]
    Max = L[0]
    for value in L:
        if value <= Min:
            Min=value
        elif value >= Max:
            Max=value    
    return(Min,Max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')