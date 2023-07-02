#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# time:2021/4/14 22:20

import time

def cal_time(func):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        result = func(*args,**kwargs)
        t2 = time.time()
        print("%s running time:%s secs." % (func.__name__,t2-t1))
        return result
    return wrapper
