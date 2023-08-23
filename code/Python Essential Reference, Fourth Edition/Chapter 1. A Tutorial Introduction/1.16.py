#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.16 Modules

# file : div.py
def divide(a,b):
    q = a/b     # If a and b are integers, q is an integer
    r = a - q*b
    return (q,r)

a, b = divide(2305, 29)
print(" %d / %d = %d --- %d" % (2305,29,a,b))

import div
a, b = div.divide(2305, 29)
print(" %d / %d = %d --- %d" % (2305,29,a,b))

import div as foo
a, b = foo.divide(2305, 29)
print(" %d / %d = %d --- %d" % (2305,29,a,b))

from div import divide
a, b = divide(2305, 29)
print(" %d / %d = %d --- %d" % (2305,29,a,b))

# To load all of module's contents into the current namespace
from div import *

import string
print(dir(string))
