#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2.7 Documentation Strings

# The indentation of the documentation string must be consistent with all
# the other statements in a definition.
def fact(n):
    "This function computes a factorial"
    if (n <= 1): return 1
    else: return n * fact(n - 1)

print(fact.__doc__)
