S = int(input())
MOD = 10 ** 9 + 7

DP = [0] * (S+1)
DP[0] = 1

for i in range(S):
	for nex in range(i+3, S+1):
		DP[nex] += DP[i]
		DP[nex] %= MOD

print(DP[S] % MOD)
