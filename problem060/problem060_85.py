n,m,l=map(int,input().split())
b=[]
for i in range(n):
    x= list(map(int, input().split()))
    b.append(x)
y=[]
for i in range(m):
    z= list(map(int, input().split()))
    y.append(z)
c = [[0] * l for i in range(n)]
for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += b[i][k] * y[k][j]
    print(*c[i])  #*をつけると[]が外れて表示される
