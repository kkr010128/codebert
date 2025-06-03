while True:
    card = input()
    if card == '-':
        break
    times = int(input())
    while times:
        h = int(input())
        card = card[h:] + card[:h]
        times -= 1
    print(card)