while True:
    card = input()
    if card == '-' : break
    n = int(input())
    for _ in range(n):
        x = int(input())
        card = card[x:len(card)] + card[0:x]
    print(card)