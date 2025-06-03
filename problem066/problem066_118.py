while True:
    cards = raw_input()
    if cards == '-':
        break
    n = input()
    for _ in xrange(n):
        h = input()
        cards = cards[h:] + cards[:h]
    print cards