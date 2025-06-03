# coding: utf-8
import sys
i = sys.stdin

for line in i:
    a,b = map(int,line.split())
    if a == 0 and b == 0: break
    if a < b:
        print(a,b)
    else:
        print(b,a)