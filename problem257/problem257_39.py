N = int(input())
Ali = list(map(int,input().split()))
s = 1
res = 0

for i in range(N):
  if Ali[i] == s:
    s += 1
  else:
    res += 1
    
if s == 1:
  print(-1)
else:
  print(res)