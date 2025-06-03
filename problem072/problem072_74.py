c, flag = 0, 0
for _ in range(int(input())):
  d1, d2 = map(int, input().split())
  if d1 == d2:
    c += 1
  else:
    c = 0
  if c >= 3:
    flag = 1
if flag:
  print("Yes")
else:
  print("No")