S=input()
n=len(S)
a=[0]*2019
MOD=2019
current=0
a[0]=1
for i in range(n):
  current=(current+int(S[n-1-i])*pow(10,i,MOD))%MOD
  a[current]+=1
ans=0
for i in range(2019):
  ans+=(a[i]*(a[i]-1))//2
print(ans)
