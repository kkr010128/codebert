# 写経
import sys

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, u, v = map(int, readline().split())
m = map(int, read().split())
AB = zip(m, m)

graph = [[] for _ in range(n + 1)]
for a, b in AB:
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    dist = [-1] * (n + 1)
    # 初期化
    stack = [v]
    # 初期位置を記憶
    dist[v] = 0
    # 初期位置の距離を0に
    while stack:
        # stackの中身がなくなるまで頑張る
        v = stack.pop()
        # stackから1つ要素を取り出す
        dw = dist[v] + 1
        # その要素の周りを考えるので、距離としてはその要素の距離に1を加えたものを考える
        for w in graph[v]:
            # 考えている要素に対して隣接している点に対して
            if dist[w] >= 0:
                # もし今まで訪れたことがあったら無視
                continue
            dist[w] = dw
            # 訪れたことがなかったら距離を更新
            stack.append(w)
            # 訪れたことがないところだったらstackに訪れる点リストとして保存
    return dist


answer = 0
du, dv = dfs(u), dfs(v)
for u, v in zip(du[1:], dv[1:]):
    if v - u > 0:
        x = v - 1
        if answer < x:
            answer = x
print(answer)
