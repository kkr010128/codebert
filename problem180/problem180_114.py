N,K = map(int,input().split())
if N % K >= abs(N % K - K):
  print(abs(N % K - K))
else:
  print(N % K)