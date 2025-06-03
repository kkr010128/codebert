A, B = map(str, input().split())
N, M = map(int, input().split())
S = input()

if A == S:
  print(N-1,M)
elif B == S:
  print(N,M-1)
