import sys
n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
f=sorted(list(map(int,input().split())),reverse=True)
h,l=max(a[i]*f[i] for i in range(n))+1,0

if sum(a)<=k: print(0);sys.exit()

while h-l>1:
    m=(h+l)//2
    practice=sum(max(0,a[i]-m//f[i]) for i in range(n))
    if practice<=k: h=m
    else: l=m
print(h)