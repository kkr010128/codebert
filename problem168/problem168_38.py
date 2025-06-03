N, M = map(int, input().split())
A = list(map(int, input().split()))

hw = sum(A)
if(N >= hw):
  print(N - hw)
else:
  print(-1)