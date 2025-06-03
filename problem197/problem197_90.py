#!/usr/bin/env python3

a, b, c = map(int, input().split())

if a+b>c:
    print('No')
    exit()


f1 = 4*a*b - 2*a*b + 2*c*a + 2*b*c
f2 = c**2 + b**2 + a**2

if f1 < f2:
    print('Yes')
else:
    print('No')
