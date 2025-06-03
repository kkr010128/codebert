N, K = map(int, input().split())

if N <= K:
  print(0)
  
else:
  H = list(map(int, input().split()))
  H.sort()
  H.reverse()
  
  c = 0
  for i in range(K, N):
    c += H[i]
  print(c)