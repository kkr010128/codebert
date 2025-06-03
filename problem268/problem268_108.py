N = int(input())
P = list(map(int, input().split()))
ans = 1
cnt = [0] * 3
mod = 10**9+7
for i in range(N):
	opt = 0
	cond = 1
	for j in range(3):
		if cnt[j] == P[i]:
			opt += 1
			if cond:
				cnt[j] += 1
				cond = 0

	ans *= opt
	ans %= mod

ans %= mod
print(ans)