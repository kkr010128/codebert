# coding: utf-8


n = int(input())

scores = [0,0]

for i in range(n):
    card = input().split()
    first_card = card[0]
    card.sort()
    if (card[0] == card[1]):
        scores[0] += 1
        scores[1] += 1
    elif(first_card == card[0]):
        scores[1] += 3
    else:
        scores[0] += 3

print(scores[0], scores[1])