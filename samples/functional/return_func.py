#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


#Test
L = list(range(1, 11))
print(L)
print(calc_sum(*L))


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum


#Test
f = lazy_sum(*L)
print(f)
print(f())

# 闭包（Closure）


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()


def count_stc():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count_stc()


#def createCounter():
#    Z=0
#    def counter():
#        nonlocal Z
#        Z=Z+1
#        return Z
#    return counter

#def createCounter():
#    def g(): #生成器生成有序数列1，2，3......
#        Z=1
#        while 1:
#            yield Z
#            Z+=1
#    a=g()
#    def counter():
#        return next(a) #每次调用next()函数获得生成器的下一个返回值
#    return counter

#def createCounter():
#    L=[0] #初始化列表L为0
#    def counter():
#        L[0]+=1 #L[0]指的是列表L的第一个元素，为一个可变变量
#        return L[0]
#    return counter

def createCounter():
    L = []

    def counter():
        L.append(1)  # 这里只是为了补位，添加任何一个数字都可以的
        return len(L)
    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


## 匿名函数
list(map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

## 匿名函数 lambda x:x*x 实际上就是:
def fun(x):
    return x*x

f = lambda x:x*x
print('把匿名函数赋值给一个变量f:',f(5))

# 匿名函数同样可以作为返回值返回
def build(x,y):
    return lambda:x*x+y*y

f=build(1,2)
print(f)
print(f())


L = list(filter(lambda n:n%2==1, range(1, 20)))
print('using lambda replace func\'is_odd\':',L)


# def now():
#     print('2021-03-07')
# 
# f = now
# a= f()
# print(a)
# print(f())
# print()
# print(now.__name__)
# 
# print(f.__name__)


# Decorator
# def log(func):
#     def wrapper(*arg,**kw):
#         print('call %s():' % func.__name__)
#         return func(*arg,**kw)
#     return wrapper
# 
# @log
# def now():
#     print('2021-03-07')
# 
# print()
# print(now())


# def log(text):
#     def decorator(func):
#         def wrapper(*arg,**kw):
#             print('%s %s():' % (text,func.__name__))
#             return func(*arg,**kw)
#         return wrapper
#     return decorator
# 
# @log('execute')    
# def now():
#     print('2021-03-14')
# 
# print(now())


