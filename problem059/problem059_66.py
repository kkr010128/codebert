r, c = map(int, input().split())
h = [[0] * c for _ in range(r + 1)]
for i in range(r):
    h[i] = list(map(int, input().split()))
for i,j in enumerate(h):
    h[i].append(sum(j))
for i in range(c + 1):
    for j in range(r):
        h[r][i] += h[j][i]
for i in h:
    print(*i)
