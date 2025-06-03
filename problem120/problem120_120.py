N,K = map(int,input().split())
P = list(map(int,input().split()))
a = 0
for i in range(K):
  a += min(P)
  del P[P.index(min(P))]
print(a)