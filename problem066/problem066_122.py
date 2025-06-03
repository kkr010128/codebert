while True:
    cards = input()
    if cards == '-':
        break
    n = int(input())
    for i in range(n):
        h = int(input())
        cards = cards[h:] + cards[:h]
    print(cards)