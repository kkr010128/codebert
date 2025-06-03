N = int(input())

if N%2 == 1 or N <= 9:
  print(0)
else:
  t = 10
  ans = 0
  while N >= t:
    ans += N//t
    t *= 5
  print(ans)