H, N = [int(_) for _ in input().split()]

A = []
ma = None

for i in range(N):
    a, b = [int(_) for _ in input().split()]
    A.append((a, b, a / b))

A.sort(key=lambda x: -x[2])
ans = 0
# ans = (H // A[0][0]) * A[0][1]
h = H # % A[0][0]

if h > 0:
    memo = [10 ** 9 + 7] * (h + 1)
    memo[h] = 0
    for j in range(h, 0, -1):
        for i in range(N):
            a, b, c = A[i]
            x = j - a
            if x < 0:
                x = 0
            memo[x] = min(memo[x], memo[j] + b)

    ans += memo[0]

print(ans)
