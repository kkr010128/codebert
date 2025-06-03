# -*- coding: utf-8 -*-

n = input()
l = map(int, raw_input().split())
for i in range(n-1):
    print l[n-i-1],
print l[0]