h,n = map(int,input().split())
p = []
inf = 10**9
for i in range(n):
    a,b = map(int,input().split())
    p.append([a,b])
m = [[0 for i in range(h)]for i in range(n+1)]
for i in range(n+1):
    for j in range(h):
        m[i][j] = inf
for i in range(n):
    for j in range(h):
        if p[i][0] >= j+1:
            m[i+1][j] = min(m[i][j],p[i][1])
        else:
            m[i+1][j] = min(m[i][j],m[i+1][j-p[i][0]]+p[i][1])
print(m[n][h-1])