#!/usr/bin/python3
#coding: utf-8

S = int(input())

memo = {}

def rec(n):
    if n < 3:
        return 0
    ret = 1
    if n in memo:
        return memo[n]

    for i in range(n-3):
        ret += rec(n-3-i)
        ret %= 10**9 + 7
    memo[n] = ret
    return ret

print(rec(S))