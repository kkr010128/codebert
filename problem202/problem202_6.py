#!/usr/bin/env python3
import sys

input = sys.stdin.readline


def ST():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(MI())


N, A, B = MI()

q, r = divmod(N, A + B)

if r > A:
    print(q * A + A)
else:
    print(q * A + r)
