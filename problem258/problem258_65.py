N = int(input())

if N % 2 == 1:
  print(0)
else:
  i = 1
  ans = 0
  while 2*(5**i) <= N:
    div = 2 * (5 ** i)
    ans += int(N//div)
    i += 1
  print(ans)