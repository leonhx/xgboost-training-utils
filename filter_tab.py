#!/usr/bin/env python

import sys

i = int(sys.argv[1])
value = sys.argv[2]

for line in sys.stdin:
    line = line.strip()
    if line.split('\t')[i] == value:
        print(line)
