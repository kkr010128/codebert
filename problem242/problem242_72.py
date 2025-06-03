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
com = [0]
for i in range(N):
    com.append(A[i] + com[-1])
#print(com)
ans = 0
for i in range(K-2,N-1):
    ans += combinations(i,K-2) * (-(com[N-i-1]) + (com[N]-com[i+1]))
    #print(N-i-1,N,i+1)
    ans %= MOD
    #print(combinations(i,K-2) * (-(com[N-i-1]) + (com[N]-com[i+1])))
print(ans)

