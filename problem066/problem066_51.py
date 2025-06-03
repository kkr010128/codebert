def shuffle(cards, h):
    return cards[h:] + cards[:h]

def solve(cards, hs):
    for h in hs:
        cards = shuffle(cards, h)
    return cards

if __name__ == '__main__':
    while True:
        s = input()
        if s == '-':
            break
        m = int(input())
        hs = [int(input()) for i in range(m)]
        print(solve(s, hs))