n, k = map(int, input().split())

MOD = 10 ** 9 + 7

def factorial(n):
    global fct
    global invfct
    fct = [0] * (n + 1)
    fct[0] = 1
    for i in range(1, n+1):
        fct[i] = fct[i-1] * i % MOD
    invfct = [0] * (n + 1)
    invfct[n] = pow(fct[n], MOD - 2, MOD)
    for i in range(n-1, -1, -1):
        invfct[i] = invfct[i+1] * (i + 1) % MOD

def binomial(n, k):
    return fct[n] * invfct[n-k] % MOD * invfct[k] % MOD

factorial(2 * n)

if k >= n:
    print(binomial(2 * n - 1, n) % MOD)
else:
    answer = 0
    for i in range(k+1):
        answer += binomial(n, i) * binomial(n-1, i)
        answer %= MOD
    print(answer)
