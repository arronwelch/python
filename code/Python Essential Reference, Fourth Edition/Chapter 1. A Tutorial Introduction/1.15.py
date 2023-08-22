#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 1.15 Exceptions

# Traceback (most recent call last):
#  File "foo.py", line 12, in <module>
# IOError: [Errno 2] No such file or directory: 'file.txt'

try:
    f = open("file.txt", "r")
except IOError as e:
    print(e)
    raise RuntimeError("Computer says no")

import threading
message_lock = threading.Lock()
# ...
with message_lock:
    message.add(newmessage)

