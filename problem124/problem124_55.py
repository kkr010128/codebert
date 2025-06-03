K = int(input())
S = input()
N = len(S)
MOD = 10**9 + 7

fct = [1]
invfct = [1]
pow25 = [1]
pow26 = [1]
for i in range(1, K+N+1):
    fct.append(fct[i-1] * i % MOD)
    invfct.append(pow(fct[i], MOD-2, MOD))
    pow25.append(pow25[i-1] * 25 % MOD)
    pow26.append(pow26[i-1] * 26 % MOD)

def cmb(n, k):
    return fct[n] * invfct[k] * invfct[n-k]

ans = 0
for i in range(K+1):
    temp = pow25[i]
    temp *= cmb(i+N-1, N-1)
    temp *= pow26[K-i]
    ans += temp
    ans %= MOD
print(ans)