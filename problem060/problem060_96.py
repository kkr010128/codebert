n,m,l = map(int,input().split())
A = []
for i in range(n):
    a = [int(j) for j in input().split()]
    A.append(a)
B = []
for j in range(m):
    b = [int(k) for k in input().split()]
    B.append(b)
    
for i in range(n):
    c = []
    for k in range(l):
        x = 0
        for j in range(m):
            x += A[i][j]*B[j][k]
        c.append(str(x))
    print(" ".join(c))