X = int(input())

year = 1
yokin = 100

while True:
    yokin += yokin//100
    if yokin >= X:
        print(year)
        break
    year += 1