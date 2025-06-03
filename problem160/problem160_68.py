import itertools
n,m,q=map(int,input().split())
a=[]
b=[]
c=[]
d=[]
for i in range(q):
    a1,b1,c1,d1=map(int,input().split())
    a.append(a1)
    b.append(b1)
    c.append(c1)
    d.append(d1)

l=list(range(1,m+1))
ans=0
for A in list(itertools.combinations_with_replacement(l, n)):
    sum=0
    for i in range(q):
        if A[b[i]-1]-A[a[i]-1]==c[i]:
            sum+=d[i]
    ans=max(ans,sum)

print(ans)

        


    



