import sys
while True:
    cards = sys.stdin.readline().strip()
    if cards == "-":
        break
    n = int(sys.stdin.readline())
    for i in range(n):
        h = int(sys.stdin.readline())
        cards = cards[h:] + cards[:h]
    print(cards)