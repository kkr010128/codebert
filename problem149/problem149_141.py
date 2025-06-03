n,m,x = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
ans = 10**9
for i in range(2 ** n):
  skill = [0] * m
  overTen = False
  money = 0
  for j in range(n):
    if ((int(bin(i)[2:]) >> j) & 1):
      money += a[j][0]
      for h in range(m):
        skill[h] += a[j][h+1]
  for k in skill:
    if k >= x:
      overTen = True
    else:
      overTen = False
      break
  if overTen == True:
    if money < ans:
      ans = money

if ans == 10**9:
  print(-1)
else:
  print(ans)