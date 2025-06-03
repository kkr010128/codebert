while True:
    c=input()
    
    if c=="-":
        break
        
    cards=list(c)
    m=int(input())
    
    for i in range(m):
        h=int(input())
        for i in range(h):
            s=cards.pop(0)
            cards+=s
    print("".join(cards))