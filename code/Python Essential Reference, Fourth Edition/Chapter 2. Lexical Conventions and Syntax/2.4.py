#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 2.4 String Literals

# String literals are used to specify a sequence of characters and defined by enclosing
# text in single('),double("),or triple('''or""") quotes.There is no semantic difference
# between quoting styles other than the requirement that you use the same type of quote to
# start and terminate a string.

# Single- and double-quoted strings must be defined on a single line, whereas triple-quoted
# strings can span multiple lines and include all of the enclosed formatting(that is,newlines,
# tabs,spaces,and so on).

# Adjacent strings (separated by white space,newline,or a line-continuation character) such as
# "hello" 'world' are concatenated to form a single string "helloworld".


print("Table 2.1 Standard Character Escape Codes")
print("Character\t\t\tDescription")
print("\t\t\tNewline \
continuation")

print("\\ \t\t\tBackslash")

print("\' \t\t\tSingle quote")

print("\" \t\t\tDouble quote")

print("\a \t\t\tBell")

print("123", end='')
print("\b \t\t\tBackspace")

# Is it a Bug?
print("\e \t\t\tEscape")

print("\0 \t\t\tNull")

print("\n \t\t\tLine feed")

print("print('hello\\vworld')\t\tVertical tab")
print('hello\vworld\tVertical tab')

print("\t \t\tHorizontal tab")

print("123", end='')
print("\rCarriage return")

print("\fForm feed")

print("\361 \t Octal value (\\000 to \\377)")

print("\u00f1 \t Unicode character (\\u0000 to \\uffff)")

print("\U000000f1 \t Unicode character (\\U00000000 to \\Uffffffff)")

print("\N{SPACE}Unicode character name:\\N{SPACE}")

print("\xf1 \t Hexadecimal value (\\x00 to \\xff)")

# escape special characters
# \xhh  # Hexadecimal value (\x00 to \xff)
print("Jalape\xf1o")

# s = u"Jalape\u00f1o" # python2 pass
# s = u"Jalape\u00f1o" # python3 syntax error

# python2 -U test.py # emulate Unicode mode, like python3

# \u U+0000 -> U+FFFF, eg:U+00F1
print("\u00f1")

# \U U+10000 and above, for example,\U00012345
print("\U00012345")

# Unicode characters also have a descriptive name.
print("Jalape\N{LATIN SMALL LETTER N WITH TILDE}o")

# http://www.unicode.org/chats
print("\u4E80")

# raw strings
print(r'\n')
print(r'c:\newdata\tests')
print(r"\u4E80")
print(r"\\u4E80")

print('Jalape\xc3\xb10')
print(b"Jalape\xc3\xb10")
