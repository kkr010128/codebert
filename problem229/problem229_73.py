HP, n = map(int, input().split())
AB = [list(map(int,input().split())) for _ in range(n)]

# DP
## DP[i]は、モンスターにダメージ量iを与えるのに必要な魔力の最小コスト
## DPの初期化
DP = [float('inf')] * (HP+1); DP[0] = 0
## HP分だけDPを回す.
for now_hp in range(HP):
    ## 全ての魔法について以下を試す.
    for damage, cost in AB:
        ### 与えるダメージは、現在のダメージ量＋魔法のダメージか体力の小さい方
        next_hp = min(now_hp+damage, HP)
        ### 今の魔法で与えるダメージ量に必要な最小コストは、->
        ####->現在わかっている値か今のHPまでの最小コスト＋今の魔法コストの小さい方
        DP[next_hp] = min(DP[next_hp], DP[now_hp]+cost)
print(DP[-1])