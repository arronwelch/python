#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# time:2021/4/12 23:18

def linear_search(li,var):
    for ind,v in enumerate(li):
        if v == var:
            return ind
    else:
        return None

list = range(10)

print(linear_search(list,5))

# time complexity:O(n)
