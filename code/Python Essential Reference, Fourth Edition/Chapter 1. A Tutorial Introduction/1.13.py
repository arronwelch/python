#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.13 Coroutines

def print_matches(matchtext):
    print("Looking for", matchtext)
    while True:
        line = (yield)  # Get a line of text
        if matchtext in line:
            print(line)

matcher = print_matches("python")
matcher.__next__()      # Advance to the first (yield)
matcher.send("Hello World")
matcher.send("python is cool")
matcher.send("yow!")
matcher.close()         # Done with the matcher function call

# A example of using generators and coroutines together:
# A set of matcher coroutines
matchers = [
    print_matches("python"),
    print_matches("guido"),
    print_matches("jython")
]

# Prep all of the matchers by calling next()
for m in matchers: m.__next__()

# tail a file (like tail -f)
import time
def tail(f):
    f.seek(0,2)     # Move to EOF
    while True:
        line = f.readline()     # Try reading a new line of text
        if not line:
            time.sleep(0.1)
            continue
        yield line

# Feed an active log file into all matchers. Note for this to work,
    # a web server must be actively writing data to the log.
wwwlog = tail(open("access-log"))
for line in wwwlog:
    for m in matchers:
        m.send(line)    # Send data into each matcher coroutine

