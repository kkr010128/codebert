N,D = map(int, input().split())
XY = [map(int, input().split()) for _ in range(N)]
X,Y = [list(i) for i in zip(*XY)]

s=0
for i in range (N):
  if X[i]*X[i]+Y[i]*Y[i]<=D*D:
    s=s+1
print(s)