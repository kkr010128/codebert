N, M = map(int, input().split())
a = [[0, 0] for i in range(N)]
for i in range(M):
  IN = list(input().split())
  p = int(IN[0])
  S = IN[1]
  if S == "AC":
    a[p-1][1] = 1
  else:
    if a[p-1][1] == 0:
      a[p-1][0] += 1
m = 0
n = 0
for i in range(N):
  if a[i][1] == 1:
    m += 1
    n += a[i][0]
print(m)
print(n)