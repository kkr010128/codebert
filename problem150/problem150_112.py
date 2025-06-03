n, k = map(int, input().split())
a = list(map(lambda x: int(x) - 1, input().split()))

table = [[0] * n for _ in [0] * 64]
table[0] = a

for i in range(61):
    for j in range(n):
        table[i + 1][j] = table[i][table[i][j]]

ans = 0
for i in range(61, -1, -1):
    if k >> i & 1:
        ans = table[i][ans]
print(ans + 1)
