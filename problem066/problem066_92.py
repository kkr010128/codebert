while True:
    deck = input()
    if deck == "-":
        break
    m = int(input())
    for i in range(m):
        h = int(input())
        deck += deck[:h]
        deck = deck[h:]
    print(deck)