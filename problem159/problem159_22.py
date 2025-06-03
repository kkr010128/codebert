X = int(input())

year = 0
amount = 100

while amount < X:
    risi = amount // 100
    amount += risi
    year += 1

print(year)
