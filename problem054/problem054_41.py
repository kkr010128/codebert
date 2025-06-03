# coding: utf-8
suits = ['S', 'H', 'C', 'D']
cards = [(suit + str(i)) for suit in suits for i in range(1, 14)]

for _ in range(int(input())):
    cards.remove(''.join(input().split()))

for trump in cards:
    print(trump[0], trump[1:])

