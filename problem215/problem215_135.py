n, k = map(int, input().split())

mod = 10 ** 9 + 7
N = n + 1

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y // 2) ** 2 % mod
    else            : return power(x, y // 2) ** 2 * x % mod

factorial = [1]
for i in range(1, N):
    factorial.append(factorial[i - 1] * i % mod)

inverseFactorial = [0] * N
inverseFactorial[N - 1] = power(factorial[N - 1], mod - 2)
for i in range(N - 2, -1, -1):
    inverseFactorial[i] = inverseFactorial[i + 1] * (i + 1) % mod

def comb(x, y):
    return factorial[x] * inverseFactorial[y] * inverseFactorial[x - y] % mod

ans = 1
for i in range(1, min(k + 1, n)):
    tmp = comb(n - 1, n - i - 1) * comb(n, i)
    ans += tmp
    ans %= mod
print(ans)
