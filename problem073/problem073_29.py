M = 10 ** 6
d = [0] * (M+1)

for a in range(1, M+1):
    for b in range(a, M+1):
        n = a * b
        if n > M:
            break
        d[n] += 2 - (a==b)


N = int(input())
ans = 0
for c in range(1, N):
    ans += d[N - c]

print(ans)