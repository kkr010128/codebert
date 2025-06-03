#!/usr/bin/env python3
import sys

s = input()
s2 = s[:(len(s) - 1) // 2]
s3 = s[(len(s) + 3) // 2 - 1 :]

if s == s[::-1]:
    if s2 == s2[::-1]:
        if s3 == s3[::-1]:
            print("Yes")
            sys.exit()

print("No")
