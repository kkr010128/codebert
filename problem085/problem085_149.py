from math import gcd
n=int(input())
a=list(map(int,input().split()))
x=[-1]*(10**6+5)
x[0]=0
x[1]=1
i=2
while i<=10**6+1:
    j=2*i
    if x[i]==-1:
        x[i]=i
        while j<=10**6+1:
            x[j]=i
            j+=i
    i+=1

z=[0]*(10**6+5)

g=gcd(a[0],a[0])
for i in range(n):
    g=gcd(g,a[i])
if g!=1:
    print("not coprime")
else:
    f=0
    for i in range(n):
        p=1
        while a[i]>=2:
            if p==x[a[i]]:
                a[i]=a[i]//p
                continue
            else:
                p=x[a[i]]
                z[p]+=1
                a[i]=a[i]//p

    for i in range(10**6+1):
        if z[i]>=2:
            f=1
    print("pairwise coprime" if f==0 else "setwise coprime")
