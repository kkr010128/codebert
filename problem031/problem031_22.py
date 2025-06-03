while True:
  n = int(input())
  s = []
  if n == 0:
    break
  s = list(map(int, input().split()))
  m = sum(s) / n
  v = 0
  for i in s:
    v += (i - m) ** 2
  ans = (v / n) ** (1/2)
  print('{:10f}'.format(ans))
