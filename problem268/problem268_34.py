n=int(input())
mod=1000000007
l=list(map(int,input().split()))
me=[3]+[0]*2*n
ans=1
for x in l:
  ans=ans*me[x]%mod
  me[x]-=1
  me[x+1]+=1
print(ans)