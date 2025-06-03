r,c = map(int,input().split())

a = [[0 for i in range(c+1)] for j in range(r+1)]

for i in range(r):
    a_tmp = list(map(int,input().split()))
    for j in range(c):
        a[i][j] = a_tmp[j]
        a[i][c] += a_tmp[j]
        a[r][j] += a_tmp[j]
        a[r][c] += a_tmp[j]

for i in range(r+1):
    print(' '.join(str(x) for x in a[i]))