x = int(input())

balance = 100
cnt = 0
while balance < x:
    balance += int(balance//100)
    cnt += 1

print(cnt)