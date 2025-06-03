N, M=map(int, input().split())
mat = [[0 for m in range(M)]for n in range(N)]
vec = [0 for m in range(M)]

for n in range(N):
  mat[n] = list(map(int , input().split()))
for m in range(M):
  vec[m] = int(input())

c = 0
for n in range(N):
 for m in range(M):
  c += mat[n][m] * vec[m]
 print(c)
 c = 0