N = int(input())
X = list(map(int,input().split()))

minimum = 10000000

for n in range(1,max(X)+1):
  kyori = 0
  for i in range(N):
    kyori += (X[i]-n)**2
  if kyori < minimum:
    minimum = kyori
print(minimum)