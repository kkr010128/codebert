import sys, math
input = sys.stdin.readline
rs = lambda: input().strip()
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
mod = 10**9 + 7

N, K = rl()
H = rl()

ans = 0
for h in H:
	if h >= K:
		ans += 1
print(ans)