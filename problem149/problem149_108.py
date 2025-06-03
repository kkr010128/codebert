N,M,X = map(int,input().split())
A = [list(map(int,input().split())) for n in range(N)]
a = 10**9

for i in range(2**N):
  S = (M+1)*[0]
  for j in range(N):
    if (i>>j)&1:
      S = [S[k]+A[j][k] for k in range(M+1)]
  if all([X<=s for s in S[1:]]):
    a = min(a,S[0])

if a==10**9:
  print(-1)
else:
  print(a)