#!/usr/bin/env python3
import sys

x = int(input())

for i in range(-10 ** 3, 10 ** 3):
    for j in range(-10 **3, 10 ** 3):
        if (i ** 5) - (j ** 5) == x:
            print(i, j)
            sys.exit()
