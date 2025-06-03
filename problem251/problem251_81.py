n,k=map(int,input().split())
s,p,r=map(int,input().split())
a=list(input())
count={}
count["s"]=s
count["p"]=p
count["r"]=r
ans=0

for i in range(k):
    for j in range(i,n,k):
        if j-k>=0 and a[j-k]!=a[j]:
            ans+=count[a[j]]
        if j-k>=0 and a[j-k]==a[j]:
            a[j]="q"
        elif j-k<0:
            ans+=count[a[j]]
        
print(ans)