MOD = 10 ** 9 + 7

K = int(input())
S = input()
l = len(S)

fac = [1] * (K + l + 1)
for i in range(1, K + l + 1):
	fac[i] = (fac[i - 1] * i) % MOD

p25 = [1] * (K + 1)
p26 = [1] * (K + 1)
for i in range(1, K + 1):
	p25[i] = (p25[i - 1] * 25) % MOD
	p26[i] = (p26[i - 1] * 26) % MOD

ans = 0
for en in range(l - 1, l + K):
	t = (fac[en] * pow(fac[en - l + 1], MOD - 2, MOD) * pow(fac[l - 1], MOD - 2, MOD)) % MOD
	t = (t * p25[en - l + 1]) % MOD
	t = (t * p26[l + K - 1 - en]) % MOD
	ans = (ans + t) % MOD
print(ans)