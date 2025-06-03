X = int(input())
P = 100
year = 0
while X > P:
    P += P // 100
    year += 1

print(year)