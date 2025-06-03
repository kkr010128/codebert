N=int(input())
a=1;b=1;c=1
MOD=10**9+7
for i in range(N):
  a=a*10%MOD
  b=b*9%MOD
  c=c*8%MOD

print((a-2*b+c)%MOD)