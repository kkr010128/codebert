all = [suit + ' ' + str(rank) for suit in 'SHCD' for rank in range(1, 14)]
for _ in range(int(input())):
    all.remove(input())
for card in all:
    print(card)
