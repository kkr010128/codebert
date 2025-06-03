n,m,l=map(int, input().split())
a=[]
b=[]
for i in range(n):
    a.append(list(map(int, input().split())))
for j in range(m):
    b.append(list(map(int, input().split())))
for i in range(n):
    ci=[0]*l
    for k in range(l):
        for j in range(m):
            ci[k]+=a[i][j]*b[j][k]
    print(*ci)
