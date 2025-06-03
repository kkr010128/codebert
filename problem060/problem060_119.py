n, m, l = list(map(lambda x: int(x), input().split(" ")))
A = list()
for i in range(n):
    A.extend([list(map(lambda x: int(x), input().split(" ")))])
B = list()
for i in range(m):
    B.extend([list(map(lambda x: int(x), input().split(" ")))])
C = list([[0 for l_ in range(l)]for n_ in range(n)])
for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]
for a in C:
    print("%d" % a[0], end="")
    for b in a[1:]:
        print(" %d" % b, end="")
    print()