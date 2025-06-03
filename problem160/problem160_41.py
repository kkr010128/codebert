from itertools import combinations_with_replacement as cr
n,m,q=map(int,input().split())
s=[list(map(int,input().split()))for i in range(q)]
f=0
for i in cr([i for i in range(1,m+1)],n):
    e=0
    for a,b,c,d in s:
        if i[b-1]-i[a-1]==c:
            e+=d
    if f<e:f=e
print(f)       