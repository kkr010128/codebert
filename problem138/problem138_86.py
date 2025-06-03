MOD = 998244353
N, S = map(int, input().split())
A = tuple(map(int, input().split()))
table = [[0] * (S + 1) for _ in range(N + 1)]
table[0][0] = 1
for n in range(N):
    for s in range(S + 1):
        now = table[n][s]
        table[n + 1][s] = (table[n + 1][s] + now * 2) % MOD
        if s + A[n] <= S:
            table[n + 1][s + A[n]] = (table[n + 1][s + A[n]] + now) % MOD
print(table[N][S])