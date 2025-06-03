n,m = map(int,input().split())
mat=[]
v=[]
for i in range(n):
    a=list(map(int,input().split()))
    mat.append(a)

for j in range(m):
    v.append(int(input()))

for i in range(n):
    w = 0
    for j in range(m):
        w += mat[i][j]*v[j]
    print(w)

