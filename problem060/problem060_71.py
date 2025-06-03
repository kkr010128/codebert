n, m, l = map(int, input().split())
A, B = [list(map(int, input().split())) for r in range(n)], [list(map(int, input().split())) for r in range(m)]
for i in range(n):
    for j in range(l):
        Cij = 0
        for k in range(m):
            Cij += A[i][k]*B[k][j]
        if j < l-1:
            print('%d' %(Cij), end=' ')
        else:
            print('%d' % (Cij))