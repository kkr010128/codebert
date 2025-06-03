#!/usr/bin/env python3
import sys
from decimal import Decimal as D

input = sys.stdin.readline


def ST():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(MI())


A, B = MI()

for i in range(1, 2501):
    a = int(D(i) * D("0.08"))
    b = int(D(i) * D("0.1"))

    if A == a and B == b:
        print(i)
        exit()

print(-1)
