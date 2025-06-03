#!/usr/bin/python3
# -*- coding: utf-8 -*-

#
# This problem can be solved smarter. But this example shows simple method
#

import sys

while True:
    s = sys.stdin.readline().strip()
    if s == '-':
        break
    n = int(sys.stdin.readline())
    for i in range(n):
        h = int(sys.stdin.readline())
        s = s[h:] + s[:h]
    print(s)

