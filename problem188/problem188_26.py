# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

X, Y, A, B, C = lr()
P = lr(); P.sort(reverse=True)
Q = lr(); Q.sort(reverse=True)
R = lr(); R.sort(reverse=True)
P = P[:X]
Q = Q[:Y]
Z = P + Q + R
Z.sort(reverse=True)
answer = sum(Z[:X+Y])
print(answer)
