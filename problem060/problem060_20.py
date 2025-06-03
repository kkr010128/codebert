n,m,l = map(int,input().split())
A = list()
B = list()
for i in range(n):
    A.append(list(map(int,input().split())))
for i in range(m):
    B.append(list(map(int,input().split())))
for i in range(n):
    C = list()
    for j in range(l):
        sum = 0
        for k in range(m):
            sum += A[i][k] * B[k][j]
        C.append(sum)
    print(" ".join(list(map(str,C))))

