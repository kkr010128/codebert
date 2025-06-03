D = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(D)]
t = [0]*D
for i in range(D):
    t[i] =int(input())
m=[0]*D
last_day=[0]*26
a=[[0 for i in range(26)] for j in range(D)]
for u in range(D):
    i=t[u]
    for y in range(u,D):
        a[y][i-1]=u+1
    if u==0:
        m[u]=s[u][i-1]
    else:
        m[u]=m[u-1]+s[u][i-1]
mm=[0]*D
for d  in range(D):
    for i in range(26):
        mm[d]+=c[i]*(d+1-a[d][i])
    if not d==0:
        mm[d]+=mm[d-1]
for d in range(D):
    m[d]-=mm[d]
    print(m[d])