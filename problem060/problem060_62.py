n, m, l = map(int, input().split())
a = []
b = []
ans = [[0 for _ in range(l)] for _ in range(n)]
for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(m):
    b.append(list(map(int, input().split())))
for i in range(n):
    for j in range(l):
        for k in range(m):
            ans[i][j] = ans[i][j] + a[i][k] * b[k][j]
for ans_row in ans:
    print(*ans_row)

