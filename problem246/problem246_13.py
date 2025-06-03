import os, sys, re, math
import itertools

N = int(input())
P = tuple([int(n) for n in input().split()])
Q = tuple([int(n) for n in input().split()])

nums = [n for n in range(1, N + 1)]
patterns = itertools.permutations(nums, N)
i = 0
for pattern in patterns:
    if pattern == P:
        pi = i
    if pattern == Q:
        qi = i
    i += 1

print(abs(pi - qi))