# modular inverse for positive a and b and nCk mod MOD depending on modinv

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

MOD = 10 ** 9 + 7

N,K = map(int,input().split())

a = list(map(int,input().split()))
a.sort()

Combination = []

for i in range(N):
    if i < K - 1:
        Combination.append(0)
    elif i == K - 1:
        Combination.append(1)
    else:
        Combination.append(Combination[-1] * i * modinv(i - K + 1, MOD) % MOD)

        
ans = 0

for i in range(N):
    ans += a[i] * Combination[i]
    ans -= a[i] * Combination[N - i - 1]
    ans %= MOD

print(ans)