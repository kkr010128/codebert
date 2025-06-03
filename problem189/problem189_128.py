N, M = map(int, input().split())
res = 0
if N >= 2:
  res += N * (N - 1) / 2
if M >= 2:
  res += M * (M - 1) / 2
print(int(res))