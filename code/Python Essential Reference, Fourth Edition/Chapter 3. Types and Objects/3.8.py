#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 3.8 Sequence Types:Lists

# list(s) | Converts s to a list.
s = 'abcd'
print('s =',s,type(s))
l = list(s)
print('l =',l,type(l))

# s.append(x) | Appends a new element,x,to the end of s.
l.append('e')
print('l =',l,type(l))

# s.extend(t) | Appends a new list,t,to the end of s.
l.extend(list('fg'))
l.extend('hi')
print('l =',l,type(l))

# s.count(x) | Counts occurrences of x in s.
print('l.count(\'i\')=',l.count('i'))
print('l.count(\'j\')=',l.count('j'))

# s.index(x [,start [,stop]]) | Returns the smallest i where s[i] == x. start
#                               and stop optionally specify the starting and ending
#                               index for the search.
print('l.index(\'c\',0,4) =',l.index('c',0,4),type(l.index('c',0,4)))

# s.insert(i,x) | Inserts x at index i.
l.insert(4,'I')
print('l.insert(4,\'I\')')
print('l =',l,type(l))

# s.pop([i]) | Returns the element i and removes it from the
#              list. If i is omitted, the last element is returned.
l.pop()
print('l.pop()')
print('l =',l,type(l))
l.pop(5)
print('l.pop(5)')
print('l =',l,type(l))

l.append('I')
print('l.append(\'I\')')
print('l =',l,type(l))
# s.remove(x) | Searches for x and removes the smallest index's it from s.
l.remove('I')
print('l =',l,type(l))

# s.reverse() | Reverses items of s in place.
l.reverse() 
print('l =',l,type(l))

# s.sort([key [, reverse]]) | Sorts items of s in place. key is a key function.
#                           | reverse is a flag that sorts the list in reverse
#                           | order. key and reverse should always be specified
#                           | as keyword arguments.
l.sort()
print('l =',l,type(l))

