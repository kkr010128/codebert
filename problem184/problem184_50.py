# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

S = sr()
bl = False
if S[2] == S[3] and S[4] == S[5]:
    bl = True

print('Yes' if bl else 'No')
