n,k=map(int,input().split())
mod=10**9+7
c=0
for i in range(k,n+2):
  min=(1/2)*i*(i-1)
  max=(1/2)*i*(2*n+1-i)
  c+=max-min+1
print(int(c%mod))