#!/usr/bin/env python3
from sys import stdin, stdout

def solve():
    n = int(stdin.readline().strip())

    seqA = []
    seqB = []
    for i in range(n):
        a,b = map(int, stdin.readline().split())
        seqA.append(a)
        seqB.append(b)

    seqA = sorted(seqA)
    seqB = sorted(seqB)
    mA = seqA[n//2]
    mB = seqB[n//2]
    if n%2==0:
        mA += seqA[n//2-1]
        mB += seqB[n//2-1]

    print(mB-mA+1)

solve()