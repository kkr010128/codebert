N, K = map(int, input().split())
MOD = 10 ** 9 + 7
ans = 0

A = list(0 for _ in range(K + 1))
B = list(0 for _ in range(K + 1))

for i in range(1, K + 1):
    A[i] = pow((K // i), N, MOD)

for i in range(K, 0, -1):
    a = 0
    for j in range(i * 2, K + 1, i):
        a += B[j]
    B[i] = A[i] - a
    B[i] %= MOD

for i in range(K + 1):
    ans += B[i] * i % MOD
    ans %= MOD
                       
print(ans)