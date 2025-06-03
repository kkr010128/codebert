N = int(input())
L = []

for _ in range(N):
    L.append(list(map(int,input().split())))

ans = 0

for i in range(N-1):
    for j in range(i + 1, N):
        ans += ((L[i][0] - L[j][0]) ** 2 + (L[i][1] - L[j][1]) ** 2) ** 0.5

ans *= 2 / N

print(ans)