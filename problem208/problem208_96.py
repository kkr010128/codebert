import sys
 
N, M = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(M)]
 
flagN = [False]*N
numN = [0]*N
if N > 1:
  numN[0] = 1

for sc in SC:
  s, c = sc[0], sc[1]
  if flagN[s-1] == False:
    flagN[s-1] = True
    numN[s-1] = c
  elif numN[s-1] == c:
    continue
  else:
    print(-1)
    sys.exit()
    
if N != 1 and numN[0] == 0:
  print(-1)
  sys.exit()

ans = ''
for n in numN:
  ans += str(n)
print(ans)