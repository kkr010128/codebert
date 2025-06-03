n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)

ans=0
for i in range(1,n+1, 2):
  if a[i]%2==1:
    ans+=1
print(ans)
