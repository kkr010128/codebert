t_HP, t_A, a_HP, a_A = map(int,input().split())
ans = False
while True:
  a_HP -= t_A
  if a_HP <= 0:
    ans = True
    break
  t_HP -= a_A
  if t_HP <= 0:
    break

if ans == True:
  print("Yes")
else:
  print("No")