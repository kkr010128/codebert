from collections import defaultdict
def solve():
  N, M = map(int, input().split())
  d = defaultdict(lambda: -1)
  for i in range(M):
    x,y = map(int, input().split())
    if d[x]>=0 and d[x]!=y:
      return -1
    if N>1 and x==1 and y==0:
      return -1
    d[x] = y
  if N==1 and d[1]==-1:
    return 0
  if d[1]==-1:
    d[1] = 1
  for i in range(2,N+1):
    if d[i]==-1:
      d[i] = 0
  ans = ''
  for i in range(1,N+1):
    ans += str(d[i])
  return ans
print(solve())