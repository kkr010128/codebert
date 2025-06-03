MAX = 600000
MOD = 10 ** 9 + 7
fac = [0] * MAX
ifac = [0] * MAX
fac[0] = 1
for i in range(1,MAX):
    fac[i] = (fac[i-1] * i) % MOD
ifac[MAX-1] = pow(fac[MAX-1],MOD-2,MOD)
for i in reversed(range(1,MAX)):
    ifac[i-1] = (ifac[i] * i) % MOD

def combinations(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return (fac[n] * ifac[k] * ifac[n-k]) % MOD

N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

def f(A):
    ans = 0
    for i in range(K-1,N):
        ans += A[i]*combinations(i,K-1)
        ans %= MOD
        #print(A[i],combinations(i,K-1))
    return ans

print((f(A) - f(list(reversed(A)))) % MOD )
#print(f(A))

