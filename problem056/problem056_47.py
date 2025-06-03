n,m = map(int,input().split())
mat = list()
vec = list()
ans = [0 for _ in range(n)]
for _ in range(n):
    mat.append(list(map(int,input().split())))
for _ in range(m):
    vec.append(int(input()))

for i in range(n):
    for j in range(m):
        ans[i] += mat[i][j]*vec[j]

for k in ans :
    print(k)