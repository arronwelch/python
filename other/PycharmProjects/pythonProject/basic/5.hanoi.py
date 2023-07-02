#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# time:2021/4/12 23:05


def hanoi(n,a,b,c):
    if n > 0:
        hanoi(n-1,a,c,b)
        print("moving from %s to %s" % (a,c))
        hanoi(n-1,b,a,c)

hanoi(3,'A','B','C')
