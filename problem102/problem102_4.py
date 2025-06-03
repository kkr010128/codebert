n,k = map(int, input().split())
scores = list(map(int, input().split()))

for i in range(k, n):
  a = scores[i]
  b = scores[i-k]
  if a > b:
    print('Yes')
  else:
    print('No')