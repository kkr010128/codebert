#!/usr/bin/env python3

import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
cnt=0
for i in range(n):
    if i%2==0 and arr[i]%2==1:
        cnt+=1
print(cnt)
