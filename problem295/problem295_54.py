n, m, L = map(int, input().split())
abc = [list(map(int, input().split())) for _ in range(m)]
q = int(input())
st = [list(map(int, input().split())) for _ in range(q)]

d = [[float('inf') for _ in range(n)] for _ in range(n)]
for a, b, c in abc:
    if c > L:
        continue
    d[a-1][b-1] = c
    d[b-1][a-1] = c

def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            if i == k or d[i][k] > L:
                continue
            for j in range(n):
                if i == j:
                    continue
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

warshall_floyd(d)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        elif d[i][j] <= L:
            d[i][j] = 1
        else:
            d[i][j] = float('inf')

warshall_floyd(d)

for s, t in st:
    if d[s-1][t-1] == float('inf'):
        print(-1)
    else:
        print(d[s-1][t-1] - 1)
