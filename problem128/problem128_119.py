x,n = map(int,input().split())
if n == 0:
  print(x)
else:
  p = list(map(int,input().split()))
  k = [i for i in range(-200,201)]
  for i in range(n):
    if p[i] in set(k):
      k.remove(p[i])
  minimum = 99999
  ans = 0
  for i in range(len(k)):
    if abs(k[i] - x )  < minimum :
      minimum = abs(k[i] - x)
      ans = k[i]
  print(ans)