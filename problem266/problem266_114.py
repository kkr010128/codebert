N = int(input())
a = N // 100
if 0 <= N - 100 * a <= 5 * a:
  print(1)
else:
  print(0)