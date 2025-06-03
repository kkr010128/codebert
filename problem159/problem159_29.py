X = int(input())
money = 100
count = 0
while True:
    count += 1
    money = (money * 100 * 101) // 10000
    if money >= X:
        print(count)
        break