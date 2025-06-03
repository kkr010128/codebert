X = int(input())

money = 100
answer = 0

while money < X:
    money += (money//100)
    answer += 1

print(answer)