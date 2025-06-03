#!/usr/bin/python3
import sys
from collections import Counter
input = lambda: sys.stdin.readline().strip()
n = int(input())
a = [int(x) for x in input().split()]
c = Counter(a)
def c2(n):
    return n * (n - 1) // 2

ans = sum(c2(v) for v in c.values())

def add(x):
    global ans
    ans -= c2(c[x])
    c[x] += 1
    ans += c2(c[x])

def remove(x):
    global ans
    ans -= c2(c[x])
    c[x] -= 1
    ans += c2(c[x])

for x in a:
    remove(x)
    print(ans)
    add(x)