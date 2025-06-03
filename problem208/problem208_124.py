import sys

N, M = map(int, input().split())
if N==1 and M == 0:
  print('0')
  sys.exit()

d={}
ans = 0
for i in range(M):
  s, c = map(int, input().split())
  if s == 1 and c == 0 and N == 1:
    ans = -2
  elif s == 1 and c == 0:
    ans = -1
  elif s in d and c != d[s]:
    ans = -1
  else:
    d[s] = c
if ans == -1:
  print(ans)
elif ans == -2:
  print('0')
else:
  for i in range(N):
    if i+1 in d:
      print(d[i+1], end='')
    elif i+1 == 1:
      print('1', end='')
    else:
      print('0', end='')