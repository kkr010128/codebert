while True:
    l = input()
    if l == '-':
        break
    deck = list(l)
    for i in range(int(input())):
        n = int(input())
        deck = deck[n:] + deck[:n]
    print(''.join(deck))