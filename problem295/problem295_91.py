
from scipy.sparse.csgraph import floyd_warshall as fw
N, M, L = map(int, input().split())

# 町間の道の長さのマトリックスを初期値無限で作成
S = [[float("INF") for i in range(N)] for i in range(N)]

# 町間の道の長さ情報をマトリックスに入力
for i in range(M):
    a, b, c = map(int,input().split())
    S[a-1][b-1] = c
    S[b-1][a-1] = c


# ワーシャルフロイド法で最短距離のマップを生成
Sf = fw(S)

T = [[float("INF")for i in range(N)] for i in range(N)]

# 町間を補給なしで通行可能な場合は1、不可能な場合はINFとしてマトリックスを作成
# （町間距離がタンク容量より大きい場合は通行不可）
for i in range(N):
    for j in range(N):
        if Sf[i][j] <= L:
            T[i][j] = 1

# ワーシャルフロイド法で町間移動可否のマップを生成
# すぐ上のfor文で、補給なしで移動できない町間の移動コストはINFにしたが、
# この処理で複数回の補給を行えば移動できる距離を
Tf = fw(T)

for i in range(int(input())):
    a, b = map(int, input().split())
    if Tf[a-1][b-1] != float("INF"):
        print(int(Tf[a-1][b-1])-1)
    else:
        print(-1)
