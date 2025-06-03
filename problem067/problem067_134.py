n = int(input())

card = ['' for i in range(n)]
score1 = 0
score2 = 0


def win(score):
    score += 3
    return score


def draw(score):
    score += 1
    return score

for i in range(n):
    card[i] = [j for j in input().split()]

for i in range(n):
    if card[i][0] == card[i][1]:
        score1 = draw(score1)
        score2 = draw(score2)
    else:
        if card[i][0] > card[i][1]:
            score1 = win(score1)
        else:
            score2 = win(score2)

print(score1,score2)