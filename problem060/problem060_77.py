n,m,l = map(int,input().split())

a = [list(map(int,input().split(" "))) for i in range(n)]

b = [list(map(int,input().split(" "))) for j in range(m)]

for i in range(n):
    for j in range(l):
        c = 0
        for k in range(m):
            c += a[i][k]*b[k][j]
        print(c,end="")
        if j != l-1:
            print("",end=" ")
    print()