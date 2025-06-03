taro_score = 0
hanako_socore = 0
game_times = int(input())
for _ in range(game_times):
    cards = input().split()
    if cards[0] > cards[1]:
        taro_score += 3
    elif cards[0] == cards[1]:
        taro_score += 1
        hanako_socore += 1
    else:
        hanako_socore += 3
print(taro_score, hanako_socore)

