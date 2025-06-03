N,M = map(int,input().split())

if N%2==1:
  for i in range(M):
    print(str(i+1) + " " + str(N-(i+1)))
else:
  flag = False
  l = 1
  r = N-1
  cnt = 0
  while cnt < M and l < r:
    if not flag and r-l <= N//2:
      r -= 1
      flag = True
    print(str(l) + " " + str(r))
    l += 1
    r -= 1
    cnt += 1