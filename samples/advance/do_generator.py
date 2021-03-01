#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 斐波拉契数列（Fibonacci）
# 除第一个和第二个数外，任意一个数都可由前两个数相加得到
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

#def fib(max):
#    n,a,b=0,0,1
#    while n<max:
#        print(b)
#        a,b=b,a+b
#        n=n+1
#    return 'done'
#
#fib(6)

def fib(max):
    n,a,b=0,0,1
    while n<max:
        #print(b)
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
# 如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator

f=fib(6)
print(next(f))

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()

# odd不是普通函数，而是generator，
# 在执行过程中，遇到yield就中断，下次又继续执行。

# for in print generator
for n in fib(6):
    print(n)

# 捕获错误
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:',e.value)
        break

# 练习
# 杨辉三角定义如下：
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

def triangles():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L,L+[0])]

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('Test Pass!')
else:
    print('Test Fail!')

    
