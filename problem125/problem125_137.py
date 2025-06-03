#!/usr/bin/env python3
x = int(input())
for i in range(360):
    k = i + 1
    if x * k % 360 == 0:
        print(k)
        exit()
