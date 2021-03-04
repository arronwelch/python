#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
    return n%2==1

print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))
# 结果: [1, 5, 9, 15]

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['A','','B',None,'C','  '])))
# 结果: ['A', 'B', 'C']

# 用filter求素数
# 埃氏筛法:
#   1.列出从2开始的所有自然数:2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#   2.取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉
#   3.取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉
#   4.取新序列的第一个数5，然后用5把序列的5的倍数筛掉
#   不断筛下去，就可以得到所有的素数。

# 构造一个从3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n #这是一个生成器，并且是一个无限序列
# 定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0
# _not_divisible(n)函数中返回的是lambda x: x % n > 0，即返回的是一个函数    

# 定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n),it)

# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# 注意到Iterator是惰性计算的序列，
# 所以我们可以用Python表示“全体自然数”，
# “全体素数”这样的序列，而代码非常简洁。

# 练习
# 回数是指从左向右读和从右向左读都是一样的数，
# 例如12321，909。请利用filter()筛选出回数：

def is_palindrome(n):
    return str(n)[::1]==str(n)[::-1]

# a=[12,3,4,5,6,7,8]
# a[::-1]
# [8, 7, 6, 5, 4, 3, 12]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')