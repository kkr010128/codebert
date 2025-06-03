while True:
    cards=input()
    if cards=="-":break
    for i in range(int(input())):
        h=int(input())
        cards=cards[h:]+cards[:h]
    print(cards)
