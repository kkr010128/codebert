r, c = list(map(int, input().split(' ')))
matrix = []
for i in range(r):
    matrix.append(input())

ans = 0
cost = {}  # cost[(i, j), (p, q)]  -> (i,j) -> (p,q) の minコスト (20 * 20 * 20 * 20 = 1.6 * 1e4)
for i in range(r):
    for j in range(c):
        if matrix[i][j] == '#':  # !!!
            continue
        start = (i, j)
        cost[(i,j), (i,j)] = 0
        q = [start]
        while q:
            ti, tj = q.pop(0)
            for ni, nj in [(ti-1, tj), (ti, tj-1), (ti+1, tj), (ti, tj+1)]:
                if ni < 0 or nj < 0 or ni >= r or nj >= c or matrix[ni][nj] == '#':
                    continue
                if cost.get(((i,j), (ni, nj)), 99999999999999999) > cost[(i,j), (ti, tj)] + 1:
                    cost[(i,j), (ni, nj)] = cost[(i,j), (ti, tj)] + 1
                    ans = max(ans, cost[(i,j), (ni, nj)])
                    #print('i,j = ', (i,j), 'ni,nj = ', (ni,nj), 'ans = ', cost[(i,j), (ni, nj)])
                    q.append((ni, nj))
print(ans)