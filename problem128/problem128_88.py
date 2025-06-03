X,N = map(int,input().split())
p = list(map(int,input().split()))

for i in range(X+1):
  for j in [-1,1]:
    a = X + i*j
    if p.count(a) == 0:
      print(a)
      exit(0)