import sys
import collections

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
#read = sys.stdin.buffer.read

N = 2100000
MAX_NUM = N + 1
MOD = pow(10, 9) + 7

fac  = [0 for _ in range(MAX_NUM)]
finv = [0 for _ in range(MAX_NUM)]
inv  = [0 for _ in range(MAX_NUM)]

fac[0]  = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1

for i in range(2,MAX_NUM):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD

def combinations(n,k):
    global fac, finv
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD

def main():
    K = int(input())
    S = input()[:-1]
    lenS = len(S)
    ans = 0
    for i in range(lenS, lenS+K+1):
        k = min(i-lenS, lenS-1)
        ans += (((combinations(i-1, k)*pow(25, i-lenS, MOD))%MOD)*pow(26, lenS+K-i, MOD))%MOD
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
