import sys
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7


K, X = rl()

if K*500 >= X:
    print('Yes')
else:
    print('No')