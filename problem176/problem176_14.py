mod = 10 ** 9 + 7

N, K = map(int, input().split())

A = [0] + [pow(K // x, N, mod) for x in range(1, K + 1)]
for x in reversed(range(1, K + 1)):
    for i in range(2, K // x + 1):
        A[x] -= A[i * x]

print(sum(i * a for i, a in enumerate(A)) % mod)