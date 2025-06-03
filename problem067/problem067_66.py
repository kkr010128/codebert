# Card Game

cardAmount = int(input())

taro = 0
hanako = 0
for i in range(cardAmount):
    cards = input().rstrip().split()
    sortedCards = sorted(cards)
    if cards[0] == cards[1]:
        taro += 1
        hanako += 1
    elif cards == sortedCards:
        hanako += 3
    else:
        taro += 3
print(taro, hanako)

