n = int(input())
coordinates = []
for _ in range(n):
    x, L = map(int, input().split())
    coordinates.append((x-L, x+L))
coordinates.sort(key=lambda x: x[1])

INF = 10**18
X = -INF
ans = 0
for L, R in coordinates:
    if L < X:
        continue
    X = R
    ans += 1
print(ans)