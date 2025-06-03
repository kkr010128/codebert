from heapq import heappush, heappop
N, M = map(int, input().split())
s = input()
INF = 10**18
dp_cnt = [INF]*(N+1)
dp_next = [0]*(N+1)
dp_cnt[N] = 0
q = [(0,N)]

for i in range(N-1, -1, -1):
  while True:
    cnt, j = q[0]
    if j-i>M:
      heappop(q)
    else:
      break
  dp_cnt[i] = cnt
  if s[i]=='1':
    cnt = INF
    j = 0
  cnt += 1
  heappush(q, (cnt, i))
  dp_next[i] = j

if dp_cnt[0]>=INF:
  print(-1)
  exit()

x = 0
ans = []
while x<N:
  y = dp_next[x]
  ans += [str(y-x)]
  x = y

print(*ans)