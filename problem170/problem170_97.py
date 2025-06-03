
N, K = map(int,input().split())
ans = 0
MOD = 10**9+7
for i in range(K,N+2):
  num = ((2*N-i+1)*i)//2 - ((i-1)*i)//2 +1
  ans+=num%MOD
ans%=MOD
print(ans)