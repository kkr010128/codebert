N,M = map(int,input().split())
SC = [list(map(int,input().split())) for _ in range(M)]

for i in range(0,1000):
  i = str(i)
  l = len(i)
  check = False
  if l == N:
    check = True
    for s, c in SC:
      if int(i[s-1]) != c:
        check = False
  if check:
    ans = int(i)
    break
else:
  ans = -1
    
print(ans)