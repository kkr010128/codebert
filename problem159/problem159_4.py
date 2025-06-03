import math

X = int(input())

year = 0
money = 100
while(money < X):
    money = money * 101//100
    year += 1

print(year)
