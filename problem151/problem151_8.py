from sys import stdin, stdout

rl = lambda: stdin.readline()
rll = lambda: stdin.readline().split()
rli = lambda: map(int, stdin.readline().split())

INF, NINF = float('inf'), float('-inf')

def binom_tables(n, q):
	fact = [1 for _ in range(n + 1)]
	inv = [1 for _ in range(n + 1)]
	for i in range(1, n+1):
		fact[i] = (fact[i-1] * i) % q
		inv[i] = pow(fact[i], q-2, q)
	return fact, inv

def main():
	MOD = 998244353
	n, m, k = rli()
	F, I = binom_tables(n, MOD)
	
	def binom(n, k, q):
		return (F[n]*((I[k]*I[n-k])%q))%q

	ans = 0
	for i in range(n-k, n+1):
		ans += (binom(n-1, i-1, MOD)*m*pow(m-1, i-1, MOD))%MOD
	print(ans % MOD)

if __name__ == "__main__":
	main()