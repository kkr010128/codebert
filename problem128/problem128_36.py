X,N = map(int, input().split())
P = list(map(int, input().split()))

table = [0] * 102
ans = X
dist = 102

for p in P:
  table[p] = 1

for i in range(102):
  if table[i] != 0:
    continue
  if abs(i - X) < dist:
    ans = i
    dist = abs(i - X)
  elif abs(i - X) == dist:
    ans = min(i, ans)

print(str(ans))