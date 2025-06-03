K = int(input())
S =input()

def cmb(n,r,p):
    if(r<0) or (n<r):
        return 0
    return fact[n]*factinv[r]*factinv[n-r]%p

p = 10 ** 9 + 7
N = 2 * 10**6+3
fact = [1] * ( N + 3)
factinv = [1] * (N + 3)
inv = [0]* (N + 3)
inv[1] = 1

for i in range(2,N+1):
    fact[i] = fact[i-1] * i % p
    inv[i] = p-inv[p % i] * (p//i) % p
    factinv[i] = factinv[i-1] * inv[i] % p

def powmod(a,n,mod):
    res = 1
    while n > 0:
        if n & 1:
            res = res * a % mod
        a = a * a % mod
        n>>=1
    return res

ss = len(S)
ans = 0
k = 1;
for i in range(K+1):
    ans += cmb(ss+K-i-1,ss-1,p) * k * powmod(25,K-i,p)
    ans %= p
    k = k * 26 % p

print(ans)