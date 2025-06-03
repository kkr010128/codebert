# -*- coding: utf-8 -*-
import sys

X = int(input().strip())
#-----
calc = {}

for i in range(-118,120):
    calc[i] = i**5


for a in range(-118,120):
    for b in range(-118,120):
        if (calc[a] - calc[b]) == X:
            print(a,b)
            sys.exit()
