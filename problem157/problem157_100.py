N = int(input())
A = list(map(int,input().split()))
P = {}
Q = {}
X = {}
for i in range(N):
  p = i+1+A[i]
  q = i+1-A[i]
  if str(p) in P:
    P[str(p)] += 1
  else:
    P[str(p)] = 1
  if str(q) in Q:
    Q[str(q)] += 1
  else:
    Q[str(q)] = 1
  X.setdefault(str(p),i+1+A[i])
  X.setdefault(str(q),i+1-A[i])

#J[a]とI[b]が等しいのが条件
#とりうる値 < 10**9を全て試す
ans = 0

for key in X.keys():
  if (key in P) and (key in Q):
  	ans += P[key] * Q[key]

print(ans)
