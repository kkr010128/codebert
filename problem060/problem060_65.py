n, m, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(m)]
for i in range(n):
    for j in range(l):
        print(sum(a[i][k] * b[k][j] for k in range(m)), end='')
        if j != l - 1:
            print(' ', end='')
    print('')