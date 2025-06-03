N, M = map(int, input().split())
S = [[0 for j in range(2)] for i in range(M)]
for i in range(M):
  X = input().split()
  S[i][0] = int(X[0])
  S[i][1] = str(X[1])
A = [0] * N
p = 0
s = 0
for i in range(M):
  if S[i][1] == "WA":
    if A[S[i][0]-1] != "x": 
      A[S[i][0]-1] += 1
  if S[i][1] == "AC":
    if A[S[i][0]-1] != "x":
      p +=  A[S[i][0]-1]
      A[S[i][0]-1] = "x"
      s += 1
arr = [s, p]
print(*arr)