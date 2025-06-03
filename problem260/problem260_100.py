import sys, math
from pprint import pprint
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

A = rl()

if sum(A) >= 22:
	print('bust')
else:
	print('win')
