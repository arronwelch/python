#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def int2(x,base=2):
    return int(x,base)

# func,*arg,**kw
import functools
int2 = functools.partial(int,base=2)#**kw

int2('10010')
#equal
kw = { 'base': 2 }
int('10010', **kw)

import functools
max2 = functools.partial(max,10)#*args

max2(5, 6, 7)
#equal
args={10,5,6,7}
max(*args)