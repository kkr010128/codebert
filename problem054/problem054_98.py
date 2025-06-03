n = int(input())
base = [mark + str(rank) for mark in ["S ", "H ", "C ", "D "] for rank in range(1,14)]
for card in [input() for i in range(n)]:
    base.remove(card)
for elem in base:
    print(elem)