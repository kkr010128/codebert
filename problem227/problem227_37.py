n,k = map(int, input().split())
H = list(map(int, input().split()))

H.sort()
H.reverse()

if n <= k:
  print(0)
else:
  print(sum(H[k:n]))
