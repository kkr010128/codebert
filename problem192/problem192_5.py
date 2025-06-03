n=int(input())
a=list(map(int,input().split()))
d={}
for i in range(n):
    if a[i] in d:
        d[a[i]]+=1
    else:
        d[a[i]]=1
ans=0
D=list(d.values())
for i in range(len(D)):
    s=D[i]*(D[i]-1)//2
    ans+=s
for i in range(n):
    print(ans-d[a[i]]+1)