N = int(input())
A = list(map(int,input().split()))
b = 1
c = 0
if A.count(0) != 0:
  print(0)
else:
  for i in range(N):
    b = b * A[i]
    if b > 10 ** 18:
      c = 1
      break
  if c == 0:
    print(b)
  else:
    print(-1)