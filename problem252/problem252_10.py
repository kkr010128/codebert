import sys

def f(x):
    p=0
    cnt=0
    for i in range(n-1,-1,-1):
        while p<n and a[i]+a[p]<x:
            p+=1
        cnt+=n-p
    return cnt

n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()

l,r=a[0]*2,a[n-1]*2
while True:
    if r-l<=1:
        if f(r)==m: md=r;break 
        else: md=l;break
        
    md=(r+l)//2
    k=f(md)
    if k==m: break
    elif k>m: l=md
    else: r=md

p=0
cnt=0
ans=0

for q in range(n-1,-1,-1):
    while p<n and a[q]+a[p]<=md:
        p+=1

    if p==n: break
    cnt+=n-p
    ans+=a[q]*(n-p)*2


ans+=(m-cnt)*md
print(ans)
