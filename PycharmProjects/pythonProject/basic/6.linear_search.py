#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# time:2021/4/12 23:18

from cal_time import *


@cal_time
def linear_search(li,var):
    for ind,v in enumerate(li):
        if v == var:
            return ind
    else:
        return None

@cal_time
def binary_search(li,val):
    left = 0;
    right = len(li) - 1;
    while left <= right:    #候选区域有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val: #查找的值在mid的左侧
            right = mid -1
        else:# li[mid] < val #查找的值在mid的右侧
            left = mid + 1
    else:
        return None

# list = range(10)
#
# print(linear_search(list,5))
#
# # time complexity:O(n)
#
# li = [1,2,3,4,5,6,7,8,9]
# print(binary_search(li,3))
#
# # O(logn) < O(n)

li = list(range(10000))
print(linear_search(li,3891))
print(binary_search(li,3891))

