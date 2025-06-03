n = int(input())
if n%2==1:
  print(0)
else:
  ans = 0
  div = 10
  pt = 1
  while div<=n:
    ans += n//div
    div *=5
  print(ans)