N, K = map(int, input().split())
H = list(map(int, input().split()))

if N <= K:
  print(0)
  exit()
  
H.sort(reverse=True)
print(sum(H[K:]))