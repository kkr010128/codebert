#!/usr/bin/env python3

n, a, b = map(int, input().split())

ans = 0
if (b-a)%2 == 0:
    ans = (b-a)//2
else:
    if a-1 >= n-b:
        ans = n + (1-a-b)//2
    else:
        ans = (a+b)//2

print(int(ans))
