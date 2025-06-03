N, M = map(int,input().split())

for i in range(1, M+1):
  a = N+1 - i
  if N % 2 == 0 and i > (N // 4):
    a -= 1
  print(i, a)
