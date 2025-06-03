from sys import stdin

score = [
    0, # Taro
    0  # Hanako
]

n = int(stdin.readline().rstrip())
for i in range(n):
    card_pair = stdin.readline().rstrip().split()
    if card_pair[0] > card_pair[1]:
        score[0] += 3
    elif card_pair[0] < card_pair[1]:
        score[1] += 3
    else:
        score[0] += 1
        score[1] += 1

print(*score)
