N,M = map(int,input().split())
H = list(map(int,input().split()))
H.insert(0,0)
S = set()

for m in range(M):
  A,B = map(int,input().split())
  if H[A]<=H[B]:
    S.add(A)
  if H[A]>=H[B]:
    S.add(B)

print(N-len(S))