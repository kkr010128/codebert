# -*- coding: utf-8 -*-
from sys import stdin
from operator import itemgetter

# stdin = open("sample.txt")

a, b, c = [int(x) for x in stdin.readline().rstrip().split()]

if c-a-b < 0:
    print("No")
else:
    if 4*a*b < (c-a-b)**2:
        print("Yes")
    else:
        print("No")