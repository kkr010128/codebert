N = input()

def f(x):
  p = 1
  i = 1
  cnt = 0
  while p > 0:
    p = x // (5**i) // 2
    cnt += p
    i += 1
  return cnt

if int(N[-1])%2 == 1:
  print(0)
else:
  print(f(int(N)))