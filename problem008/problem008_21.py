N = int(input())
M = []
for i in range(N):
    a = list(map(int,input().strip().split()))
    b = [int(i+1 in a[2:]) for i in range(N)]
    M.append(b)

time = 1
D = [-1 for _ in range(N)]
F = [-1 for _ in range(N)]
def dfs(src):
    global time # 関数内でglobal変数の書き換えることを宣言
    D[src] = time # 訪問時刻を記録
    time += 1
    for dst in range(N):
        # srcからdstに移動可能で、dstが未訪問だったら
        if M[src][dst] == 1 and D[dst] == -1:
            dfs(dst)
    F[src] = time # 訪問終了時刻を記録
    time += 1
    # 関数の終わりで親に戻る(青矢印)

for root in range(N):
    # 番号が若い節点から
    if D[root] == -1:
        # D[root]が未訪問だったら
        dfs(root) # dfsを始める

[print(i+1, D[i], F[i]) for i in range(N)]

