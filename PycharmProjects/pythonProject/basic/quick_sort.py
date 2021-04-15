#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# time:2021/4/16 0:23

def partition(li,left,right):
    tmp = li[left] #取出left位的数，留出空位开始切片
    while left < right:#至少有两个元素
        while left < right and li[right] >= tmp: #从右边开始找比tmp小的数，找到或者指针移到left位置推出循环
            right -= 1 #往左走一位
        li[left] = li[right] #把右边小于tmp的值放到空位left 或者 自己赋值给自己 注意right变成空位了
        print(li,left,right)
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]  # 把左边大于tmp的值放到空位right 或者 自己赋值给自己
        print(li,left,right)
    li[left] = tmp #把tmp写回空位

li = [5,7,4,6,3,1,2,9,8]
print(li)
print('//'+'-'*30+'//')

partition(li,0,len(li)-1)

print('//'+'-'*30+'//')
print(li)

