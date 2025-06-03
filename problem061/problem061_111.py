# coding: utf-8

import sys

strings = input()

for s in strings:
    if s.islower():
        sys.stdout.write(s.upper())
    else:
        sys.stdout.write(s.lower())
print()