N = int(input())
X = list(map(int, input().split()))
al = []
for i in range(100):
  d = 0
  p = i+1
  for j in range(N):
    d += (X[j]-p)**2
  al.append(d)

print(min(al))