N, T = map(int, input().split())
ls = []
for i in range(N):
  a, b = map(int, input().split())
  ls += [(a,b)]
ls.sort(key=lambda x:x[0])
t = [[0]*T for i in range(N+1)]
for i in range(1,N+1):
  a, b = ls[i-1]
  for j in range(T):
    if j-a>=0:
      t[i][j] = max(t[i-1][j-a]+b,t[i-1][j])
last = [0]
for i in range(N-1,-1,-1):
  last += [max(last[-1], ls[i][-1])]
ans = 0
for i in range(1,N+1):
  j = N-i
  ans = max(ans, last[j]+t[i][-1])
print(ans)