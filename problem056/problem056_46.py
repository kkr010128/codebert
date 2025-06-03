n,m = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for j in range(n)]
b = [0 for i in range(m)]
c = [0 for i in range(n)]
for i in range(m):
    b[i] = int(input())
for i in range(n):
        for j in range(m):
            c[i] += a[i][j] * b[j]
print('\n'.join(map(str,c)))