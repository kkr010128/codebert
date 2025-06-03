#!/usr/bin/env python3

N = int(input())

if N % 2 == 1:
    print(0)
else:
    ret = 0
    for i in range(1, 27):
        ret += N // (2*5**i)


    print(ret)
