while True:
    deck = input()
    if deck == '-':
        break
    m = int(input())
    h = [int(input()) for i in range(m)]
    for i in h:
        deck = deck[i:] + deck[:i]
    print(deck)
