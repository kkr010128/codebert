while True:
    cards = input()
    if cards == '-':
        break
    num = int(input())
    for i in range(num):
        sha = int(input())
        pre = cards[:sha]
        post = cards[sha:]
        cards = post + pre
    print(cards)
