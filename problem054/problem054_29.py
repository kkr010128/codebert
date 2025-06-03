cards = [[False] * 14 for i in range(4)]
n = int(input())
for i in range(n):
    suit, rank = input().split()
    r = int(rank)
    if suit == "S":
        s = 0
    elif suit == "H":
        s = 1
    elif suit == "C":
        s = 2
    else:
        s = 3
    cards[s][r] = True

name = ["S", "H", "C", "D"]
for s in range(4):
    for r in range(1, 14):
        if not cards[s][r]:
            print(name[s], r)