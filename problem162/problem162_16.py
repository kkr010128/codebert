N,M = map(int, input().split())
ans = []
if N%2==1:
  for i in range(2,N//2+2):
    ans.append((i,N+2-i))
else:
  l = 2
  r = N
  while r-l>N//2:
    ans.append((l,r))
    l += 1
    r -= 1
  l += 1
  while r>l:
    ans.append((l,r))
    l += 1
    r -= 1
for i in range(M):
  print(*ans[i])