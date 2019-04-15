#!/usr/bin/env python

import sys

i = int(sys.argv[1])

for line in sys.stdin:
    print(line.strip().split('\t')[i])
