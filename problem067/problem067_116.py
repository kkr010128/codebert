n = int(input())
t_score = 0
h_score = 0

for i in range(n):
    t_card, h_card = input().split()
    if t_card < h_card:
        h_score += 3
    elif t_card > h_card:
        t_score += 3
    else:
        h_score += 1
        t_score += 1

print(t_score, h_score)
