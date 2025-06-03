mod=10**9+7
k=int(input())
s=input()
l=len(s)
fact=[1]
for i in range(1,k+l+1):
  fact.append((fact[-1]*i)%mod)
revfact=[]
for i in range(k+l+1):
  revfact.append(pow(fact[i],mod-2,mod))
pows=[1]
for i in range(1,k+l+1):
  pows.append((pows[-1]*25)%mod)
ans=0
for i in range(l,l+k+1):
  ans+=fact[l+k]*revfact[i]*revfact[l+k-i]*pows[l+k-i]
  ans%=mod
print(ans)