from operator import itemgetter
import bisect
N, D, A = map(int, input().split())
enemies = sorted([list(map(int, input().split())) for i in range(N)], key=itemgetter(0))
d_enemy = [enemy[0] for enemy in enemies]
b_left = bisect.bisect_left
logs = []
logs_S = [0, ]
ans = 0
for i, enemy in enumerate(enemies):
    X, hp = enemy

    start_i = b_left(logs, X-2*D)
    count = logs_S[-1] - logs_S[start_i]

    hp -= count * A
    if hp > 0:
        attack_num = (hp + A-1) // A
        logs.append(X)
        logs_S.append(logs_S[-1]+attack_num)
        ans += attack_num
print(ans)




