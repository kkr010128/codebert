n=int(input())
l=sorted(list(map(int,input().split())))
for i,x in enumerate(l):
  l[i]=format(x,'63b')
memo=[0]*63
for i in range(63):
  for j in range(n):
    if l[j][i]=='1':
      memo[-i-1]+=1
now=1
ans=0
mod=10**9+7
for x in memo:
  ans+=(now*x*(n-x))%mod
  now*=2
print(ans%mod)
