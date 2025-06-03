def sum_part(N, k):
  return k*(2*N-k+1)/2-k*(k-1)/2+1
  
N, K = map(int, input().split())
ans = 0
for k in range(K,N+2):
  ans += sum_part(N, k)
  
ans = ans % (10**9 + 7)
  
print(int(ans))