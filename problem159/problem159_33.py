X = int(input())
money = 100
time = 0

while money < X:
  time += 1
  money = money * 101 // 100
  
print(time)