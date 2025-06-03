cards = [[0 for i in range(13)] for j in range(4)]
n = int(input())
for i in range(n):
    card = list(input().split())
    card[1] = int(card[1])
    if card[0] == 'S':
        suit = 0 
    elif card[0] == 'H':
        suit = 1 
    elif card[0] == 'C':
        suit = 2 
    elif card[0] == 'D':
        suit = 3 
    cards[suit][card[1]-1] = 1 
for i in range(4):
    if i == 0:
        suit = 'S' 
    elif i == 1:
        suit = 'H' 
    elif i == 2:
        suit = 'C' 
    elif i == 3:
        suit = 'D' 
    for j in range(13):
        if not(cards[i][j]):
            print(suit, j+1)