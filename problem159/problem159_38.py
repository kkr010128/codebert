X = int(input())
bank = 100
cnt = 0
while bank < X:
    bank = bank + bank//100
    cnt += 1
print(cnt)
