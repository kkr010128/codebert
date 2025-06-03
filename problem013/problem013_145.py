#!/usr/bin/env python3
#coding:utf-8

n = int(input())
ans = -10000000000
mini = 10000000000

for i in range(n):
    x = int(input())
    ans = ans if (x-mini) < ans else x-mini
    mini = mini if x > mini else x

print(ans)
