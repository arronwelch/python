#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.5 Strings

a = "Hello World"
b = 'Python is groovy'
c = """Computer says 'No'"""

print(a)
print(b)
print(c)

print('')

print('''Content-type: text/html
<h1> Hello World </h1>
Click <a href="http://www.python.org">here</a>.
''')

print('')

print("""Content-type: text/html
<h1> Hello World </h1>
Click <a href="http://www.python.org">here</a>.
""")

a = "Hello World"
b = a[4]        # b = 'o'
print("b = '%c'" % b)

c = a[:5]       # c = "Hello"
d = a[6:]       # d = "World"
e = a[3:8]      # e = "lo Wo"

print("c = \"%s\"" % c)
print("d = \"%s\"" % d)
print("e = \"%s\"" % e)

# Strings concatenated : plus(+) operator
g = a + " This is a test"
print(g)

x = "37"
y = "42"
z = x + y # z = "3742" (String Concatenation)
print("z = \"%s\"" % z)

z = int(x) + int(y) # z = 79 (Integer +)
print("z = %d is %s" % (z,type(z)))

x = 3.4
s = "The value of x is " + str(x)
print(s)

s = "The value of x is " + repr(x)
print(s)

s = "The value of x is " + format(x, "0.5f")
print(s)
