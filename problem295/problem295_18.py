def warshall_floyd(v_count: int, matrix: list) -> list:
    """ ワーシャルフロイド
    v_count: 頂点数
    matrix: 隣接行列(到達不能はfloat("inf"))
    """
    for i in range(v_count):
        for j, c2 in enumerate(row[i] for row in matrix):
            for k, (c1, c3) in enumerate(zip(matrix[j], matrix[i])):
                if c1 > c2+c3:
                    matrix[j][k] = c2+c3
    return matrix


INF = 10 ** 16
n, m, l = map(int, input().split())
mat = [[INF] * n for _ in range(n)]
for i in range(n):
    mat[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    mat[a - 1][b - 1] = c
    mat[b - 1][a - 1] = c
mat = warshall_floyd(n, mat)
fuel_mat = [[INF] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            fuel_mat[i][j] = 0
        elif mat[i][j] <= l:
            fuel_mat[i][j] = 1
fuel_mat = warshall_floyd(n, fuel_mat)
q = int(input())
for _ in range(q):
    s, t = map(int, input().split())
    d = fuel_mat[s - 1][t - 1]
    if d == INF:
        print(-1)
    else:
        print(d - 1)
