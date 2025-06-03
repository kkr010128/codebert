#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import string

alphabet = string.ascii_lowercase
char_count = dict()
for c in alphabet:
    char_count[c] = 0

for s in sys.stdin:
    s = s.strip().lower()
    for c in s:
        if c in alphabet:
            char_count[c] += 1

for c in alphabet:
    print(c, ':', char_count[c])

