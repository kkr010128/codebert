H, N = map(int, input().split())
A = list(map(int, input().split()))


def answer(H: int, N: int, A: list) -> str:
    damage = 0                          # damageに0を代入します
    for i in range(0, N):               # 0:Nの間にiがある間は
        damage += int(A[i])             # damageにリスト[i]をint(整数）に変え足します
                                        # 6でdamage=0にforの間Aの値を足していく意味
        i += 1                          # 条件を満たす間はiに1つずつ足していきます。リスト内を進めていく
    if damage < H:
        return 'No'
    else:
        return 'Yes'

print(answer(H, N, A))
