K = int(input())
S = input()

mod = 10**9 + 7

class Combination:
    def __init__(self, n):
        self.facts = [1 for i in range(n+1)]
        self.invs = [1 for i in range(n+1)]
        
        for i in range(1, n+1):
            self.facts[i] = self.facts[i-1] * i % mod
            self.invs[i] = pow(self.facts[i], mod-2, mod)

    def ncr(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        else:
            return self.facts[n] * self.invs[r] * self.invs[n-r] % mod

    def nhr(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0
        else:
            return self.ncr(n+r-1, n-1)

N = K+len(S)
pow25 = [1] * (N+1)
pow26 = [1] * (N+1)
for i in range(1, N+1):
    pow25[i] = (pow25[i-1] * 25) % mod
    pow26[i] = (pow26[i-1] * 26) % mod

comb = Combination(K+len(S))

ans = 0
for i in range(K+1):
    ans = (ans + comb.ncr(N-i-1, len(S)-1) * pow25[N-i-len(S)] * pow26[i]) % mod

print(ans)