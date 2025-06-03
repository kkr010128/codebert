N,K=map(int, input().split())

sum_ = 0
for k in range(K, N+2):
  sum_ += k*(N-k+1)+1
  sum_ = sum_ % (10**9+7)

print(sum_)