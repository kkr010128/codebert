n=int(input())
a=list(map(int,input().split()))

bit_l=[0 for _ in range(60)]

for x in a:
  for i in range(60):
    if ((x>>i)&1):
      bit_l[i]+=1
ans=0
mod=10**9+7
for y in range(len(bit_l)):
  r=2**y
  k=(n-bit_l[y])*bit_l[y]
  ans+=r*k%mod
  
print(ans%mod)