n,k=map(int,input().split())
sunu=[0]*n
for i in range(k):
    d=int(input())
    a=list(map(int,input().split()))
    for j in range(d):
        sunu[a[j]-1]+=1
ans=0
for i in range(len(sunu)):
    if sunu[i]==0:
        ans+=1
print(ans)                