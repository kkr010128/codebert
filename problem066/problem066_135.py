while 1:
    cards = raw_input()

    if cards == "-":
        break

    m = int(raw_input())

    for i in range(m):
        h = int(raw_input())

        for j in range(h):
            cards += cards[0]
            cards = cards[1:]

    print(cards)