N, K = [int(x) for x in input().split()]
r, s, p = [int(x) for x in input().split()]

win_point = {
    'r': r,
    's': s,
    'p': p,
}

next_hands = {
    'r': ['s', 'p'],
    's': ['r', 'p'],
    'p': ['r', 's'],
}

enemy_hands = input()


def can_win(enemy_hand, my_hands):
    # 勝てる場合にはTrueと勝てる手を教えてくれる
    if enemy_hand == 'r' and 'p' in my_hands:
        return True, 'p'
    if enemy_hand == 's' and 'r' in my_hands:
        return True, 'r'
    if enemy_hand == 'p' and 's' in my_hands:
        return True, 's'

    # 勝てる手がない場合
    return False, None


point = 0

for index in range(K):
    now_hands = ['r', 'p', 's']
    for i in range(index, N, K):
        win, hand = can_win(enemy_hands[i], now_hands)

        if win:
            point += win_point[hand]
            now_hands = next_hands[hand]
        else:
            # 勝てない場合次似邪魔しない手を選ぶ
            # 勝てない回の次は必ず勝てるため全手出せる前提とする
            now_hands = ['r', 'p', 's']

print(point)
