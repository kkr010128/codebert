n,k=map(int,input().split())
ans=[0 for _ in range(n*3)]
ans[1]=1

idou=[]

for _ in range(k):
  a=list(map(int,input().split()))
  idou.append(a)
  
    
mod=998244353

rui=[0 for _ in range(n+1)]
rui[1]=1
  
for i in range(2,n+1):
  for g in idou:
    x,y=g
    left=max(0,i-y-1)
    right=max(0,i-x)
    ans[i]+=(rui[right]-rui[left])%mod

    
  rui[i]+=((rui[i-1]+ans[i]))%mod

    
    

print(ans[n]%mod)
  
