#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Variables and Arithmetic Expressions

# python3 1.2.py
# Listing 1.1 Simple Compound-Interest Calculation
principal = 1000; rate = 0.05; numyears = 5;
year = 1
while year <= numyears:
	principal = principal * (1 + rate)
	print(year, principal) # Remider: print(year, principal) in Python 3
	year += 1

