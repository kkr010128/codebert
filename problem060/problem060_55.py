#ITP1_7_D
n,m,l=map(int,input().split())
a=[]
b=[]
for _ in range(n):
    a.append(list(map(int,input().split())))
for _ in range(m):
    b.append(list(map(int,input().split())))

c=[[0 for _ in range(l)] for _ in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j]+=a[i][k]*b[k][j]

for i in range(n):
    for j in range(l-1):
        print(c[i][j],end=" ")
    print(c[i][-1])
