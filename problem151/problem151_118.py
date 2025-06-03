MOD = 998244353

N, M, K = map(int, input().split())

fac = [1] * N
for i in range(1, N):
	fac[i] = (fac[i - 1] * i) % MOD

pow_mmm = [1] * N
for i in range(1, N):
	pow_mmm[i] = (pow_mmm[i - 1] * (M - 1)) % MOD

ans = 0
for i in range(K + 1):
	t = (M * pow_mmm[N - 1 - i]) % MOD
	comb = (fac[N - 1] * pow(fac[N - 1 - i], MOD - 2, MOD) * pow(fac[i], MOD - 2, MOD)) % MOD
	t = (t * comb) % MOD
	ans = (ans + t) % MOD
print(ans)