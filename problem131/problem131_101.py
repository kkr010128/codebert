#!/usr/bin/env python

a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())

if v <= w:
    print('NO')
    exit()
if abs(b-a)/(v-w) > t:
    print('NO')
    exit()
print('YES')
