N, K = map(int, input().split())
A = N // K
B = N % K
if B > abs(B-K):
  print(abs(B-K))
else:
  print(B)