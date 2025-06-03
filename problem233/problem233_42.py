N = int(input())
P = list(map(int, input().split()))
m = P[0]
S = 0
for p in P:
  if m>=p:
    S += 1
  m = min(m, p)
print(S)