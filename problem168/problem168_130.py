N,M=list(map(int, input().split()))
A=list(map(int, input().split()))
s=sum(A)
if s>N:
  print(-1)
else:
  print(N-s)