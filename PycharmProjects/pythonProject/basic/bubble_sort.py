#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# time:2021/4/15 0:24

import random

def bubble_sort(li):
    for i in range(len(li)-1):
        exchange = False
        for j in range(len(li)-i-1):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
                exchange = True
        print(li)
        if not exchange:#if not exchange,return
            return


li = [1,2,3,4,5,6,7,8,9]
print(li)
print()
bubble_sort(li)

print()
print(li)

