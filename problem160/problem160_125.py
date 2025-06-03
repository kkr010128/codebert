import itertools
n,m,q=map(int,input().split())
L=list(itertools.combinations_with_replacement(range(m),n))
a=[0]*q
b=[0]*q
c=[0]*q
d=[0]*q
for i in range(q):
    a[i],b[i],c[i],d[i]=map(int,input().split())
    a[i]-=1
    b[i]-=1
ans=0
for l in L:
    tmp=0
    for i in range(q):
        if l[b[i]]-l[a[i]]==c[i]:
            tmp+=d[i]
    ans=max(ans,tmp)
print(ans)