n,k=map(int,input().split())

mod=10**9+7
ans=0
for x in range(k,n+2):
  min_a=(0+x-1)*x//2
  max_a=(n-x+1+n)*x//2
  aa=max_a-min_a+1
  ans+=aa
  
print(ans%mod)