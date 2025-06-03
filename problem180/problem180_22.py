n,k = list(map(int,input().split()))

tmp = n % k

if tmp <= abs(tmp - k):
  print(tmp)
else:
  print(abs(tmp - k))