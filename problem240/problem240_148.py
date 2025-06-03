N, M = map(int, input().split())
WA = [0] * (N+1)
AC = [0] * (N+1)
Q = [list(input().split()) for _ in range(M)]
for p, s in Q:
  p = int(p)
  if AC[p] == 1:
    continue
  if s == "WA":
    WA[p] += 1
  else:
    AC[p] = 1
ans = 0
for w, a in zip(WA, AC):
  if a:
    ans += w
print(sum(AC), ans)