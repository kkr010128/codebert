suit = ['S', 'H', 'C', 'D']
cards = [[i, j] for i in suit for j in map(str, range(1, 14))]
for i in range(input()):
    cards.remove(raw_input().split())
for i in cards:
    print i[0],i[1]