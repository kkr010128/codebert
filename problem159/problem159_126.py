x=int(input())
cnt=0
money = 100
while(1):
  cnt += 1
  money += money//100
  if money >= x:
    print(cnt)
    quit()