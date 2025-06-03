#!/usr/bin/env python

x = int(input())

n = x//100

for i in range(n+1):
    tmp = x 
    tmp -= i*100
    if 5*i >= tmp:
        print(1)
        exit()
print(0)
