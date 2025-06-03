n,m=map(int,input().split())
l=[0]*(n+1)
miss=[0]*(n+1)
for _ in range(m):
    p,s=input().split()
    p=int(p)
    if l[p]==0:
        if s=='AC':
            l[p]+=1
        else:
            miss[p]+=1
for i in range(1,n+1):
    if l[i]==0 and miss[i]!=0:
        miss[i]=0
a=l.count(1)
b=sum(miss)
print(a,b)