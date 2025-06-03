import sys

N = int(input())
A = list(map(int,input().split()))


if A.count(1) == 0:
  print(-1)
  sys.exit()
else:
  
  cnt = 0
  for a in range(len(A)):
    if A[a] == cnt+1:
      cnt += 1
  print(len(A)-cnt)

