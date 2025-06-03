n,k=map(int,input().split())
L=list(map(int,input().split()))
ans=0
for i in L:
  if i>=k:
    ans+=1
    
print(ans)