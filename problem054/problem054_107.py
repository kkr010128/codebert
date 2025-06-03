cards = [[0 for i in range(13)] for j in range(4)]
s2n = {'S': 0, 'H': 1, 'C': 2, 'D': 3}
n2s = 'SHCD'
n = int(input())
for i in range(n):
    card = list(input().split())
    card[1] = int(card[1])
    cards[s2n[card[0]]][card[1]-1] = 1
for i in range(4): 
    for j in range(13):
        if not(cards[i][j]):
            print(n2s[i], j+1)