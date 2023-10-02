#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 3.6 Built-in Types for Representing Data

# 3.6.1 The None Type
s = "this is string"
if(isinstance(s, str)):
    print("\"",s,"\" is str Type")
else:
    print("\"",s,"\" is None Type")

n = None
if(isinstance(n, type)):
    print("\"",n,"\" is type")
else:
    print("\"",n,"\" not is type")
