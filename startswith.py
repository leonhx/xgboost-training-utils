#!/usr/bin/env python

import sys

argc = len(sys.argv)
assert argc == 2 or argc == 3
if argc == 2:
    match = True
    s = sys.argv[1]
elif argc == 3:
    s = sys.argv[2]
    if sys.argv[1] == '-m':
        match = True
    elif sys.argv[1] == '-u':
        match = False
    else:
        raise AssertionError("only supports -m or -u")

for line in sys.stdin:
    line = line.strip()
    if match:
        if line.startswith(s):
            print(line)
    else:
        if not line.startswith(s):
            print(line)
