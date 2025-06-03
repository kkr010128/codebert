S,T = input().split()
N,M = list(map(int, input().split()))
U = input()

if U == S:
  N = N - 1

if U == T:
  M = M - 1

print(N, M)

