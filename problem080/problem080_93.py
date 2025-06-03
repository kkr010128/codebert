#!/usr/bin/env python

n = int(input())
x_plus_y = [0 for _ in range(n)]
x_minus_y = [0 for _ in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    x_plus_y[i] = x+y 
    x_minus_y[i] = x-y 

ans = max(max(x_plus_y)-min(x_plus_y), max(x_minus_y)-min(x_minus_y))
print(ans)
