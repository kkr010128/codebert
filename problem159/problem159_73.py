x = int(input())
money = 100
ans = 0
while True:
  if money >= x:
    break
  else:
    money += money//100
    ans += 1

print(ans)