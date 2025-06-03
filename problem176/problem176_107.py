N, K = map(int, input().split())
MOD = 10**9 + 7

ans = 0
A = [0 for _ in range(K+1)]
for i in range(1,K+1):
  ans += pow(K//i, N, MOD) * (i - A[i])
  ans %= MOD
  #print(ans, i)
  
  j = 2*i
  while j <= K:
    A[j] += i - A[i]
    j += i
    
print(ans)