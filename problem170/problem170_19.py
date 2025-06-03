def mips():
  return map(int,input().split())
N,K = mips()
ans = 0
for i in range(K,N+1):
    Max_K = (i * (2*N - (i-1)))//2
    Min_K = (i * (2*0 + (i-1)))//2
    ans += (Max_K-Min_K) + 1
    ans %= (10**9 + 7)
print(ans+1)