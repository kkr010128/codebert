import os, sys, re, math

N = int(input())
P = [int(n) for n in input().split()]

answer = 0
m = 2 * 10 ** 5
for p in P:
    if p <= m:
        answer += 1
        m = p

print(answer)
