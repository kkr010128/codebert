# -*- coding: utf-8 -*-

N = int(raw_input())
for i in range(N):
    a, b, c = map(int, raw_input().split())
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    if a*a+b*b == c*c:
        print "YES"
    else:
        print "NO"