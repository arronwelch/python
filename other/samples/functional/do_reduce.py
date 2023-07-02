#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce
#
#CHAR_TO_INT = {
#    '0':0,
#    '1':1,
#    '2':2,
#    '3':3,
#    '4':4,
#    '5':5,
#    '6':6,
#    '7':7,
#    '8':8,
#    '9':9,
#}
#
#def str2int(s):
#    ints = map(lambda ch:CHAR_TO_INT[ch],s)
#    return reduce(lambda x,y:x*10+y ,ints)
#
#print(str2int('0'))
#print(str2int('12300'))
#print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '.':-1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch],s)
    point = 0
    def to_float(f,n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f*10+n
        else:
            point = point * 10
            return f+n/point
    return reduce(to_float,nums,0.0)

#print(str2float('0'))
#print(str2float('123.456'))
#print(str2float('123.45600'))
#print(str2float('0.1234'))
print(str2float('.1234'))
#print(str2float('120.0034'))

# https://www.pynote.net/archives/1145

# 从Python3开始，reduce函数不再内置，而是放入了functools模块内，
# 可能是因为此函数的应用场景没有别的内置函数那么多吧。
# reduce函数的功能，是将一个序列中的所有元素，按照顺序进行一个指定的操作，
# 最后得到一个确定的返回值。

# from functools import reduce
# # reduce definition
# reduce(function, sequence [, initial] ) -> value

# >>> a = [1,2,3,4,5]
# >>> reduce(lambda x,y:x+y, a)
# 15
# >>> reduce(lambda x,y:x+y, a, 10)
# 25

# >>> reduce(lambda x,y:x+y+'.', 'abcdefg')
# 'ab.c.d.e.f.g.'
# >>> reduce(lambda x,y:x+y+'.', 'abcdefg', '')
# 'a.b.c.d.e.f.g.'