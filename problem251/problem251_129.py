N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = list(input())

graph = {"r":P,"s":R,"p":S,"*":0}

for i,t in enumerate(T):
  if len(T)-i-K > 0:
    if t == T[i+K]:
      T[i+K] = "*"

ans = 0
for t in T:
  ans += graph[t]
print(ans)