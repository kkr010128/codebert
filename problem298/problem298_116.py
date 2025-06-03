n,k=map(int,input().split())
lis=list(map(int,input().split()))
lis.sort()
ans=0
for i in lis:
    if i<k:
        ans+=1
    else:
        
        break
print(n-ans)