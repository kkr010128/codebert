X,N = map(int,input().split())
P = list(map(int,input().split()))

for n in range(100):
  if X-n not in P:
    print(X-n)
    break
  if X+n not in P:
    print(X+n)
    break