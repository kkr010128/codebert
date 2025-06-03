N, M = map(int, input().split())
A = list(map(int, input().split()))
for Ai in A:
  N -= Ai
  if N < 0:
    print(-1)
    break
if N >= 0:
  print(N)