def nishin(n):
  return str(bin(n)[2:])[::-1]
N=int(input())
L=list(map(int,input().split()))
mod=1000000007
ans=sum(L)*(N-1)
c=[0]*61
for i in L:
  i=nishin(i)
  for j in range(len(i)):
    if i[j]=="1":
      c[j]+=1
for i in range(61):
  ans-=(pow(2,i,mod)*c[i]*(c[i]-1))%mod
print(ans%mod)