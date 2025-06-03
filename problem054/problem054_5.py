cards = []
suits = ['S', 'H', 'C', 'D']

for i in range(len(suits)):
    for j in range(1, 14):
        cards.append(suits[i] + ' ' + str(j))

n = int(input())

for i in range(n):
    cards.remove(input())

for i in range(len(cards)):
    print(cards[i])