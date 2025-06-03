from collections import deque

N = int(input())                            # 頂点数

conj = [[] for _ in range(N)]
for i in range(N):                          # 各頂点での進める先の候補の集合
    L = list(map(int, input().split()))
    for a in L[2:]:
        conj[i].append(a-1)         # 頂点番号をデクリメント

start = 0

visit = [False]*N                           # 訪れたかどうかをメモ
second_visit = [False]*N                    # 二度目に訪れた事をメモ
next_set = deque()                          # 次に進む候補を列挙する。スタック（右から取り出す = pop）だと深さ優先になり、キュー（左から取り出す = popleft）だと幅優先になる
next_set.append((start, 0))                 # スタート地点を決める。第二成分は時刻を表す。
visit[start] = True                         # スタート地点は最初から踏んでいる。
res = [-1 for _ in range(N)]
res[0] = 0

while next_set:                             # p = [] になったら止める
    p, t = next_set.popleft()               # 要素を消去して、消去した要素を出力
    for q in conj[p]:                       # 頂点 p から進める経路の候補から一つ選ぶ
        if not visit[q]:                    # 訪れた事がない場所のみ進む。壁などの条件がある場合は、ここに " grid[p] != 壁 " 等を追加する
            visit[q] = True                 # 頂点 q に一度訪れた事をメモ (for の前に書くと、ここで選ばれた q が最短であるはずなのに、違う経路でvisit = Trueを踏んでしまう可能性がある)
            res[q] = t + 1
            next_set.append((q, t + 1))     # p から q へと移動。時刻を 1 進める


for i in range(N):
    print(i+1, res[i])
