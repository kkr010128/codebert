N = int(input())
M = [""] * N
T = [0] * N

for i in range(N):
  m, t = input().split(" ")
  M[i] = m
  T[i] = int(t)

X = input()

id = M.index(X)
s = sum(T[id+1:])
print(s)