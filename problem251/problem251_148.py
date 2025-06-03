N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = list(input())

POINT = {"r":P,"s":R,"p":S}
GET = [False] * N

ANS = 0
for i in range(N):
  t = T[i]
  if i <= K-1:
    ANS += POINT[t]
    GET[i] = True
  else:
    if not GET[i-K] or t != T[i-K]:
      ANS += POINT[t]
      GET[i] = True

print(ANS)
