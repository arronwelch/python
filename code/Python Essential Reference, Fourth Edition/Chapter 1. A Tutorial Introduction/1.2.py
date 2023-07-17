#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Variables and Arithmetic Expressions

# python3 1.2.py
# Listing 1.1 Simple Compound-Interest Calculation

print ("1-----")
principal = 1000; rate = 0.05; numyears = 5;
year = 1
while year <= numyears:
    principal = principal * (1 + rate)
    print (year, principal) # Remider: print(year, principal) in Python 3
    year += 1

print ("2-----")
principal = 1000; rate = 0.05; numyears = 5;
year = 1
while year <= numyears:
    principal = principal * (1 + rate)
    print ("%3d %0.2f" % (year, principal)) # Python 3
    year += 1

print ("3-----")
principal = 1000; rate = 0.05; numyears = 5;
year = 1
while year <= numyears:
    principal = principal * (1 + rate)
    print (format(year,"3d"),format(principal,"0.2f")) # Python 3
    year += 1

print ("4-----")
principal = 1000; rate = 0.05; numyears = 5;
year = 1
while year <= numyears:
    principal = principal * (1 + rate)
    print ("{0:3d} {1:0.2f}".format(year,principal)) # Python 3
    year += 1
