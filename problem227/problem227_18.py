N, K = map(int, input().split())
H = list(map(int, input().split()))
if K >= N:
  print(0)
else:
  H = sorted(H)
  count = 0
  for i in range(N-K):
    count += H[i]
  print(count)