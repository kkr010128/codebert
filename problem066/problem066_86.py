while True:
    c = input()
    if c == "-":
        break
    card = [x for x in c]
    N = int(input())
    for n in range(N):
        h = int(input())
        card = card[h:] + card[:h]
    print("".join(map(str,card)))
    
