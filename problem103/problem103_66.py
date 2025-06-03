n = int(input())
pricies = list(map(int, input().split()))
m = 1000
stocks = 0
ask = 0

for i in range(n):
    price = pricies[i]
    isHigher = False
    isLower = False

    if stocks > 0:
        if price >= ask:
            m += price * stocks
            stocks = 0

    for j in range(i+1, n):
        if pricies[j] >= price:
            isHigher = True
            break
        else:
            isLower = True

    if isHigher and not isLower:
        stocks, m = stocks + m // price, m % price
        ask = price

print(m)