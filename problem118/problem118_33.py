# D - Sum of Divisors
N = int(input())

# 1と自分自身はかならず約数になるので、計算から除外
f = [2] * (N + 1)

for i in range(2, N//2 + 1):
	j = 2
	
	while True:
		if i * j <= N:
			f[i*j] += 1
			j += 1
		else:
			break

ans = 1

for i in range(2, N + 1):
	ans += f[i] * i

print(ans)
