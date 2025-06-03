n,m = map(int, input().split())
num = [0]*n
tf = True
for _ in range(m):
  d = list(map(int, input().split()))
  if d[0]==1 and d[1]==0 and n>1:
    tf = False
    break
  if num[d[0]-1] == 0:
    num[d[0]-1] = d[1]
    continue
  if num[d[0]-1] != d[1]: 
    tf = False
if num[0]==0 and n>1:
  num[0] = 1
if tf:
  ans = 0
  for i in range(n-1,-1,-1):
    ans += num[(n-1)-i]*(10**i)
  print(ans)
else: print(-1)