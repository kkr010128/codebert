import sys

N = int(sys.stdin.readline().strip())
X = sys.stdin.readline().strip()

def popcount(n):
    cnt = 0
    while n > 0:
        cnt += n & 1
        n //= 2
    return cnt

def f(n):
    cnt = 0
    while n != 0:
        n = n % popcount(n)
        cnt += 1
    return cnt

#nX = int(X, 2)
pcnt = X.count('1')
MOD1 = pcnt + 1
MOD2 = pcnt - 1

nXp = 0
nXm = 0

pow1 = [1] * N
pow2 = [0] * N
for i in range(1, N):
    pow1[i] = (pow1[i-1] * 2) % MOD1
if MOD2 != 0:
    pow2[0] = 1
    for i in range(1, N):
        pow2[i] = (pow2[i-1] * 2) % MOD2

for i in range(N):
    if X[i] == '1':
        nXp += pow1[N-1-i]
nXp %= MOD1

if MOD2 != 0:
    for i in range(N):
        if X[i] == '1':
            nXm += pow2[N-1-i]

    nXm %= MOD2
    

for i in range(0, N):
    if X[i] == '0':
        k = (nXp + pow1[N-1-i]) % MOD1
        print(f(k) + 1)
    else:
        if MOD2 == 0:
            print(0)
        else:
            k = (nXm - pow2[N-1-i]) % MOD2
            print(f(k) + 1)