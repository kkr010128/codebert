#!/usr/bin/env python

n, k = map(int, input().split())
a = list(map(int ,input().split()))

def check(x):
    now = 0 
    for i in range(n):
        now += (a[i]-1)//x
    return now <= k

l = 0 
r = int(1e9)
while r-l > 1:
    mid = (l+r)//2

    if check(mid):
        r = mid 
    else:
        l = mid 

print(r)