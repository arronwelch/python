#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 3.7 Sequence Types

# Sequences represent ordered sets of objects indexed by non-negative integers and include
# strings, lists and typles. Strings are sequences of characters, and lists and tuples are
# sequences of arbitrary Python objects. Strings and tuples are immutable; lists allow inser-
# tion, deletion, and substitution of elements. All sequences support iteration.

# Operations Common to All Sequences
# s[i]
s = 'abcdefg'
print('s = ',s)
print('s[2] = ',s[2])
# s[i:j]
print('s[2:3] = ',s[2:3])
print('s[2:4] = ',s[2:4])

# s[i:j:stride]
print('s[2::2] = ',s[2::2])
