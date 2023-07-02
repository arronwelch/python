#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# time:2021/4/16 0:00

# O(n^2)
def inser_sort(li):
    for i in range(1,len(li)):#i 表示摸到的牌的下标
        tmp = li[i]
        j = i -1 # j指的手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp
        print(li)

li = [3,2,4,1,5,7,9,6,8]
print(li)
print()

inser_sort(li)
#print(li)
