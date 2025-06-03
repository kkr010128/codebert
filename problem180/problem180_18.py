N,K=map(int, input().split())
if K>=N:
  print(min(N, K-N))
else:
  res = N % K
  print(min(res, K-res))