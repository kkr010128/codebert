import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
#mod = 10**9 + 7
mod = 998244353

A, B = rl()

if 1 <= A <= 9 and 1 <= B <= 9:
	print(A*B)
else:
	print(-1)
