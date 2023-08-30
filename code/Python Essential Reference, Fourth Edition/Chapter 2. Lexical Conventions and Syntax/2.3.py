#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2.3 Numeric Literals

# - Booleans:True, False
if True:
    print("True type is:",type(True))
if not False:
    print("False type is:",type(False))

# - Integers
# decimal integer: 1234
print("1234 type is:",type(1234))

# octal: 0644
print("0o644 type is:",type(0o644))
    # SyntaxError: leading zeros in decimal integer literals are not permitted;
    # use an 0o prefix for octal integers
print("0o644 value is:",0o644)

# hexadecimal: 0x100fea8
print("0x100fea8 type is:",type(0x100fea8))
print("0x100fea8 value is",0x100fea8)

# binary notation: 0b11101010
print("0b11101010 type is:",type(0b11101010))
print("0b11101010 value is:",0b11101010)

# Integers in Python can have an arbitrary number of digits
print("12345678901234567890 type is:",type(12345678901234567890))
print("12345678901234567890 value is:",12345678901234567890)
# print("12345678901234567890L value is:",12345678901234567890L) # old Python code
# print("12345678901234567890l value is:",12345678901234567890l) # old Python code

# - Floating-point numbers
print("123.34 type is:",type(123.34))
print("1.2334e+02 value is:",1.2334e+02)

# - Complex numbers
print("12.34J type is:",type(12.34J))
print("12.34J value is:",12.34J)

print("1.2 + 12.34J type is:",type(1.2 + 12.34J))
print("1.2 + 12.34J value is:",1.2 + 12.34J)

