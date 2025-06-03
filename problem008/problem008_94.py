N = int(input())
DG = {}
node_ls = []
is_visited = {}
#有効グラフをdictで管理することにする
for _ in range(N):
    tmp = input().split()
    node_id = tmp[0]
    node_ls.append(node_id)
    is_visited[node_id] = False
    adj_num = int(tmp[1])#各頂点の次元が入っている
    if adj_num != 0:
        DG[node_id] = tmp[2:]
    else:
        DG[node_id] = []


d = {}#最初に発見したときの時刻を記録
f = {}#隣接リストを調べ終えたときの完了時刻を記録
t = 1

def dfs(node):
    global t
    #終了条件
    if is_visited[node]:
        return

    is_visited[node] = True
    d[node] = t
    t += 1
    for no in DG[node]:
        dfs(no)
    f[node] = t
    t += 1

for node in node_ls:
    dfs(node)

#print(d,f)
for node in node_ls:
    print(node, d[node], f[node])

