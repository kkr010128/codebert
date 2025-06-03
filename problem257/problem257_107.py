n=int(input())
a=list(map(int,input().split()))
ans=0
res=False
res2=1
for i in range(n):
    if a[i]==res2:
        res=True
        res2+=1

ans=n-res2+1 if res else -1
print(ans)
