#!/usr/bin/env python
from __future__ import division, print_function
from sys import stdin


def fibo(n):
    a, b = 1, 1
    while n:
        a, b = b, a + b
        n -= 1
    return a


print(fibo(int(stdin.readline())))