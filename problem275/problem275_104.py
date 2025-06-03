#!/usr/bin/env python3
x,y = map(int,input().split())
if x == 1 and y == 1:
#if False:
    print(10**6)
else:
    print((max(0,4-x)+max(0,4-y))*(10**5))