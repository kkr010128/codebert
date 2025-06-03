N, M = map(int, input().split())

res = []

if N % 2 == 0:
    x = 0
    for i in range(N // 2 // 2):
        res.append((x + 1, (x + 2 * i + 1) % N + 1))
        x -= 1
        x %= N
    for i in range((N // 2 - 1) // 2):
        res.append((x + 1, (x - (N // 2 - 1) // 2 * 2 + 2 * i) % N + 1))
        x -= 1
        x %= N

else:
    for i in range(N // 2):
        res.append((i + 1, N - i - 1))

for i in range(M):
    a, b = res[i]
    print(a, b)