from math import sqrt
N = int(input())
X = []
Y = []
for i in range(N):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)
ans = 0
for i in range(0, N-1):
  for j in range(i+1, N):
    ans += sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)
print(ans * 2.0 / N)