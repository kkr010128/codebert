S,H,C,D = [],[],[],[]

def adding(card):
    if card[0] == 'S':
        S.append(int(card[1]))
    else:
        if card[0] == 'H':
            H.append(int(card[1]))
        else:
            if card[0] == 'C':
                C.append(int(card[1]))
            else:
                if card[0] == 'D':
                    D.append(int(card[1]))

def sort():
    S.sort()
    H.sort()
    C.sort()
    D.sort()

def check(pattern,cards):
    answer=[]
    for i in range(1,13+1):
        if not (i in cards):
            print pattern,i


if __name__ == '__main__':
    number = input()
    for i in range(number):
        card = map(str,raw_input().split())
        adding(card)
    sort()
    check('S',S)
    check('H',H)
    check('C',C)
    check('D',D)