#coding: utf-8
a, v = map(int,input().split())
b, w = map(int,input().split())
t = int(input())

dist = abs(a-b)
dist += (t*w)

if dist <= v*t:
    print('YES')
else:
    print('NO')