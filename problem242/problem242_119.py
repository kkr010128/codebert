import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
import numpy as np

N, K = map(int, input().split())
A = np.array(list(map(int, input().split())), dtype = np.int64)

MOD = 10**9+7
def cumprod(x, MOD = MOD):
	L = len(x)
	Lsq = int(L**.5 + 1)
	x = np.resize(x, Lsq ** 2).reshape(Lsq, Lsq)
	for n in range(1, Lsq):
		x[:,n] *= x[:,n-1]
		x[:,n] %= MOD
	for n in range(1,Lsq):
		x[n] *= x[n-1, -1]
		x[n] %= MOD
	return x.flatten()[:L]

def make_fact(U, MOD = MOD):
	x = np.arange(U, dtype = np.int64)
	x[0] = 1
	fact = cumprod(x, MOD)
	x = np.arange(U, 0, -1, dtype = np.int64)
	x[0] = pow(int(fact[-1]), MOD - 2, MOD)
	fact_inv = cumprod(x, MOD)[::-1]
	return fact, fact_inv

fact, inv = make_fact(N+100, MOD)
A.sort()
ans = 0
lim = N - K + 1
for ind, a in enumerate(A, 1):
	if ind < K:
		tmp_max = 0
	else:
		max_comb = (fact[ind-1] * inv[K-1]) % MOD * inv[ind-K] % MOD
		tmp_max = max_comb * a % MOD
	if ind > lim:
		tmp_min = 0
	else:
		min_comb = (fact[N - ind] * inv[K-1]) % MOD * inv[N - ind - K + 1] % MOD
		tmp_min = min_comb * a % MOD

	ans += (tmp_max - tmp_min) % MOD
	ans %= MOD

print(ans)