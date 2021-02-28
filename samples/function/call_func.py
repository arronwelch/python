#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#x = abs(100)
#y = abs(-20)
#print(x,y)
#print('max(1,2,3)=',max(1,2,3))
#print('min(1,2,3)=',min(1,2,3))
#print('sum([1,2,3])=',sum([1,2,3]))

#def my_abs(x):
#    if x >= 0:
#        return x
#    else:
#        return -x
#
#print(my_abs(-156))     
#
# 空函数
#def nop():
#    pass
#
#nop()
#
#if age >= 18:
#    pass

#def my_abs(x):
#    if not isinstance(x,(int,float)):
#        raise TypeError('bad operand type')
#    if x >= 0:
#        return x
#    else:
#        return -x

#import math
#
#def move(x,y,step,angle=0):
#    nx = x + step * math.cos(angle)
#    ny = y - step * math.sin(angle)
#    return nx,ny
#
#x, y = move(100, 100, 60, math.pi / 6)  
#print(x, y)

#import math
#
#def quadratic(a, b, c):
#    return ( (-b+math.sqrt(b**2-4*a*c) )/(2*a) ,(-b-math.sqrt(b**2-4*a*c) )/(2*a)   )
#
#print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
#print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
#
#if quadratic(2, 3, 1) != (-0.5, -1.0):
#    print('测试失败')
#elif quadratic(1, 3, -4) != (1.0, -4.0):
#    print('测试失败')
#else:
#    print('测试成功')

#位置参数
#def power(x):
#    return x*x
#
#def power(x,n):
#    s = 1
#    while n > 0:
#        n = n - 1
#        s = s * x
#    return s
#
#def power(x,n=2):
#    s = 1
#    while n > 0:
#        n = n - 1
#        s = s * x
#    return s
#
#def enroll(name,gender):
#    print('name:',name)
#    print('gender:',gender)
#
#def enroll(name,gender,age=6,city='Beijing'):
#    print('name:',name)
#    print('gender:',gender)
#    print('age:',age)
#    print('city:',city)
#
#def add_end(L=[]):
#    L.append('END')
#    return L
#
##默认参数
#def add_end(L=None):
#    if L is None:
#        L=[]
#    L.append('END')
#    return L
#
#def calc(numbers):
#    sum = 0
#    for n in numbers:
#        sum = sum + n*n
#    return sum
#
##可变参数
#def calc(*numbers):
#    sum = 0
#    for n in numbers:
#        sum = sum + n*n
#    return sum
#
##关键字参数 key:word
#
#def  person(name,age,**kw):
#    if 'city' in kw:
#        #有city参数
#        pass
#    if 'job' in kw:
#        pass
#    
#    print('name:',name,'age:',age,'other:',kw)

#命名关键字参数
def person(name,age,*,city,job):
    print(name,age,city,job)

def person(name,age,*args,city,job):
    print(name,age,args,city,job)

def product(*numbers):
    if not numbers:
        raise TypeError()
    sum = 1
    for n in numbers:
        sum = sum * n
    return sum


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
