import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

def main():
    K = int(input())
    S = input()
    
    M = len(S)
    N = M + K
    MAXN = N + 2
    fact = [1]
    for i in range(1,MAXN + 1):
        fact.append(fact[-1]*i%MOD)
    inv_fact = [-1] * (MAXN + 1)
    inv_fact[-1] = pow(fact[-1],MOD - 2,MOD)
    for i in range(MAXN - 1,-1,-1):
        inv_fact[i] = inv_fact[i + 1]*(i + 1)%MOD
    
    nck = lambda N,K: 0 if K > N or K < 0 else fact[N]*inv_fact[N - K]*inv_fact[K]%MOD
    
    power25 = [1]
    power26 = [1]
    for i in range(N):
        power25.append(power25[-1]*25%MOD)
        power26.append(power26[-1]*26%MOD)
    
    ans = 0
    for i in range(M,N + 1):
        ans += nck(i - 1,M - 1) * power25[i - M] * power26[N - i] % MOD
        ans %= MOD
    print(ans)
if __name__ == '__main__':
    main()