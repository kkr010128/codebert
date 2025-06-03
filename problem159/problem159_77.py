import math

X = int(input())
ans = 0
money = 100 #初期金額

while money < X:
    money += money//100
    ans += 1
    
print(ans)    
