#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# time:2021/4/15 23:31

# O(n^2)
def select_sort_simple(li):
    li_new=[]
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new

def select_sort(li):
    for i in range(len(li)-1): # i是第几趟
        min_loc = i #无序区第一个数的位置下标
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i],li[min_loc] = li[min_loc],li[i]
        print(li,i)



li = [3,4,2,1,5,6,8,7,9]
#print(select_sort_simple(li))
print(li)
select_sort(li)
#print(li)

