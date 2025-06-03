x = int(input())
money = 100
count = 0
while money < x:
    money = (money * 101) // 100
    count += 1

print(count)