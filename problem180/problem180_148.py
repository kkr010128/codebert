N,K =map(int, input().split())
a = N % K
if a > K / 2:
  print(K - a)
else:
  print(a)