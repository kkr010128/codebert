mod = 10**9+7
M = 2*10**6

fact = [1]*(M+1)
factinv = [1]*(M+1)
inv = [1]*(M+1)
for n in range(2,M+1):
    fact[n] = n*fact[n-1]%mod
    inv[n] = -inv[mod%n]*(mod//n)%mod
    factinv[n] = inv[n]*factinv[n-1]%mod

def comb(n,k):
    return fact[n]*factinv[k]*factinv[n-k]%mod

def main(K,S):
    n = len(S)
    ans = 0

    for k in range(K+1):
        ans += comb(n+k-1,k)*pow(25,k,mod)*pow(26,K-k,mod)
        ans %= mod
    print(ans)

if __name__ == '__main__':
    K = int(input())
    S = input()
    main(K,S)