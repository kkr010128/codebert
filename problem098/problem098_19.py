N = int(input())
c = input()
W = 0
R = c.count('R')
if R == 0 or R == N:
  print(0)
  exit()
ans = N
t = 0
for i in range(N):
  if c[i] == 'W':
    W += 1
  else:
    R -= 1
  t = max(R,W)
  ans = min(ans, t)
print(ans)