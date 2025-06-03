import sys

SUITS = ['S', 'H', 'C', 'D']
exist_cards = {suit:[] for suit in SUITS}

n = input()

for line in sys.stdin:
    suit, number = line.split()
    exist_cards[suit].append(int(number))


for suit in SUITS:
    for i in range(1, 14):
        if i not in exist_cards[suit]:
            print(suit, i)