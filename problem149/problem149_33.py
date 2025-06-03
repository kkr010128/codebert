n,m,x=[int(x) for x in input().split()]
b=[]
for i in range(n):
    c=[int(x) for x in input().split()]
    b.append(c)

import itertools
l=[]
a=itertools.product(range(2),repeat=n)
for i in a:
    l.append(i)

ans=5000000
e=0

for i in range(2**n):
    skill=[0]*m
    p=0
    for j in range(n):
        if l[i][j]==1:
            p+=b[j][0]
            for k in range(m):
                skill[k]+=b[j][k+1]
    s=min(skill)
    if s>=x:
        e=1
        ans=min(ans,p)
if e==1:
    print(ans)
else:
    print(-1)