# -*- coding: utf-8 -*-

import sys
import os


word = input().strip().lower()
c = 0
for s in sys.stdin:
    s = s.lower()
    for separated in s.split():
        if word == separated:
            c += 1
print(c)