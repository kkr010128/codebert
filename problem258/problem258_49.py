N = int(input())
if N%2 != 0:
  print(0)
else:
  answer = 0
  m = 10
  while m <= N:
    answer += N//m
    m *= 5
  print(answer)