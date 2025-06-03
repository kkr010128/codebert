n,m,x=map(int,input().split())
c=[list(map(int,input().split())) for _ in range(n)]
import itertools
sum_min=10**7
for i in itertools.product([0,1],repeat=n):
    level=[0]*m
    for j in range(m):
        level[j]=sum(i[k]*c[k][j+1] for k in range(n))
    for l in range(m):
        if level[l]<x:
            break
    else:
        sum_min=min(sum_min,sum(i[k]*c[k][0] for k in range(n)))
print(sum_min if sum_min!=10**7 else -1)