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

# 3.6.2.1 Numeric Types: Booleans
print(1 > 0)
print(-1 > 0)
a = -1
print('a = ', a)
a = 1 > 0
print('a = ', a)

# 3.6.2.2 Numeric Types: Integers
a = -2147483648
print('a = ',a,type(a))
b = 2147483647+1 # In Python3, the two types have been unified into a single integer type
print('b = ',b,type(b))

# 3.6.2.3 Numeric Types: Floating-point numbers
a = 1.2345
print('a = ',a,type(a))
b = 1.2345e-30 - 1e-43
print('b = ',b,type(b))

# 3.6.2.4 Complex numbers
z = 1.2 + 3.4j
print('z = ',z,type(z))
print('z.conjugate() = ',z.conjugate(),type(z.conjugate()))

x = 12345
print('x.numerator = ',x.numerator,type(x.numerator))
print('x.denominator = ',x.denominator,type(x.denominator))

y = 1.2345
print('y.real = ',y.real,type(y.real))
print('y.imag = ',y.imag,type(y.imag))
print('y.conjugate() = ',y.conjugate(),type(y.conjugate()))

print('y.as_integer_ratio() = ',y.as_integer_ratio(),type(y.as_integer_ratio()))
print('y.is_integer() = ',y.is_integer(),type(y.is_integer()))
print('y.hex() = ',y.hex(),type(y.hex()))
print("y.fromhex('0x1.3c0831') = ",y.fromhex('0x1.3c0831'),type(y.fromhex('0x1.3c0831')))
