# -*- coding: utf-8 -*-

n = int(input())
s = list(input().split())
n = int(input())
t = list(input().split())
cnt = 0
for i in range(n):
    if t[i] in s:
        cnt += 1

print(cnt)
