n, m, l = map(int, input().split())
A = [[] for a in range(n)]
B = [[] for b in range(m)]
C = [[0 for c in range(l)] for d in range(n)]
for a in A:
    a += list(map(int, input().split()))
for b in B:
    b += list(map(int, input().split()))
for k,x in enumerate(C):
    for y in range(l):
        for z in range(m):
            C[k][y] += A[k][z]*B[z][y]
for x in C:
    for k,y in enumerate(x):
        if k == l-1:
            print(y)
        else:
            print(y,end=" ")


