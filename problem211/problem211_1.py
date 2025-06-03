# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N, R = lr()
answer = R
if N < 10:
    answer += (10-N) * 100
print(answer)
