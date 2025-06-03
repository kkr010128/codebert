N = int(input())

if N % 2 == 1:
  print(0)
else:
  rlt = 0
  i = 10
  while N // i > 0:
    rlt += N // i
    i *= 5
  print(rlt)