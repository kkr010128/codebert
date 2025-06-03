N, K = map(int, input().split(' '))
P = tuple(map(int, input().split(' ')))

values = [0]

for p in P:
    values.append(values[-1] + (p * (p + 1) // 2 / p))

ans = 0
for i in range(K, N + 1):
    ans = max(ans, values[i] - values[i - K])

print(ans)
