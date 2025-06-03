n, k = map(int, input().split())
MOD = 10 ** 9 + 7

a = [0] *(k+1)

for x in range(1, k + 1):
    a[x] = pow(k // x, n, MOD)

for x in range(k, 0, -1):
    for i in range(2, k // x + 1):
        a[x] -= a[x * i]

answer = sum([i * x for i,x in enumerate(a)])

print(answer % MOD)