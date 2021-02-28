#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式即List Comprehensions，
# 是Python内置的非常简单却强大的可以用来创建list的生成式。

print([x * x for x in range(1,11)])

print([x * x for x in range(1,11) if x % 2 ==0 ])

print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x':'A','y':'B','z':'C'}

print([k + '=' + v for k,v in d.items()])

L = ['Hello','World','IBM','Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
print(L1)

L2=[s.lower() for s in L1 if isinstance(s,str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')