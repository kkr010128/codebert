MOD = 10**9 + 7
MAX = 10**6
X, Y = map(int, input().split())
m, n = 2*Y-X, 2*X-Y
if (X+Y) % 3 != 0 or m%3!=0 or n%3!=0 or m<0 or n<0:
    print(0)
    exit()

m //= 3
n //= 3

fac, inv = [0]*MAX, [0]*MAX
fac[0] = 1
for i in range(1, MAX):
    fac[i] = fac[i-1] * i % MOD
inv[-1] = pow(fac[-1], MOD-2, MOD)
for i in range(MAX-2, 0, -1):
    inv[i] = inv[i+1] * (i+1) % MOD

def com(n, k):
    if n<k:return 0
    if n<0 or k<0:return 0
    if n==k or k==0:return 1
    return int(fac[n] * (inv[k]*inv[n-k]%MOD) % MOD)

print(com(n=m+n,k=n))