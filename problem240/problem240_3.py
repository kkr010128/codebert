N,M = (int(x) for x in input().split())
AC = [False]*N
WA_count = [0]*N
AC_count = 0
for i in range(M):
  p,S = (y for y in input().split())
  if AC[int(p)-1] == False:
    if S == 'AC':
      AC[int(p)-1] = True
      AC_count += 1
    else:
      WA_count[int(p)-1] += 1
for i in range(N):
  if AC[i] == False:
    WA_count[i] = 0
print(AC_count,sum(WA_count))