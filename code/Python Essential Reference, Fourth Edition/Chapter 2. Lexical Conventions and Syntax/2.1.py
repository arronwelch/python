#!/usr/bin/python3

# Line Structure and Indentation

import math
x = 1.2
y = 2.3
n = 3.4
# line-continuation character : (\)
a = math.cos(3 * (x - n)) + \
    math.sin(3 * (y - n))

print("a = ",a)

# Indentation must be consistent
# if a:
#     statement1  # Consistent indentation
#     statement2
# else:
#     statement3
#         statement4  # Inconsistent indentation (error)

# body can be placed on the same line
# if a:   statement1
# else:   statement2

# use pass statement to denote an empty body or block
# if a:
#     pass
# else:
#     statements

# use of spaces is universally preferred(and encouraged)

# Running Python with the -t option prints warning messages when
# tabs and spaces are mixed inconsistently within the same program block.

# The -tt option turns these warning messages into TabError exceptions.

# To place more than one statement on a line, separate the statements with
# a semi-conlon(;).

# The # character denotes a comment

# the interpreter ignores all blank lines except when running in interactive mode
# In this case, a blank line signals the end of input when typing a statement that
# spans multiple lines.
