#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Conditionals

# python3 1.3.py
a = 1
b = 2
if a < b:
    print("Computer says Yes")
else:
    print("Computer says No")

a = 2
b = 1
if a < b:
    print("Computer says Yes")
else:
    print("Computer says No")

if a < b:
    pass # Do nothing
else:
    print("Computer says No(pass test)")

product = "game"
type = "priate memory"
age = 5
if product == "game" and type == "priate memory" \
                     and not (age < 4 or age > 8):
    print("I'll take it!")

suffix = ".pat"

if suffix == ".htm":
    content = "text/html"
elif suffix == ".jpg":
    content = "image/jpeg"
elif suffix == ".png":
    content = "imgage/png"
else:
    raise RuntimeError("Unknow content type")
