X = int(input())
money = 100
for i in range(1, 10000):
    money = money * 101 // 100
    if money >= X:
        print(i)
        exit()
