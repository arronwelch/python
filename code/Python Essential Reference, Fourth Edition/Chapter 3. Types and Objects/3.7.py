#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 3.7 Sequence Types

# Sequences represent ordered sets of objects indexed by non-negative integers and include
# strings, lists and typles. Strings are sequences of characters, and lists and tuples are
# sequences of arbitrary Python objects. Strings and tuples are immutable; lists allow inser-
# tion, deletion, and substitution of elements. All sequences support iteration.

# Operations Common to All Sequences

# s[i] | Returns element i of a sequence
s = 'abcdefg'
print('s = ',s)
print('s[2] = ',s[2])

# s[i:j] | Returns a slice
print('s[2:3] = ',s[2:3])
print('s[2:4] = ',s[2:4])

# s[i:j:stride] | Returns an extended slice
print('s[2::2] = ',s[2::2])

# len(s) | Number of elements in s
print('len(s) = ', len(s))

# min(s) | Minimum value in s
print('min(s) = ', min(s))

# max(s) | Maximum value in s
print('max(s) = ', max(s))

s = [1,2,3,4,5,6,7]
print('s = ',s)
# sum(s [, initial]) | Sum of items in s
print('sum(s) = ', sum(s))

# all(s) | Checks whether all items in s are True.
print('all(s) = ', all(s))

# any(s) | Checks whether any item in s is True.
print('any(s) = ', any(s))
