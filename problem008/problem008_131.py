cin = open(0).read().strip().split('\n')
n = int(cin[0])
g = [list(map(lambda x: int(x)-1, a.split(' ')[2:])) for a in cin[1:]]

first_order = [-1] * n
last_order = [-1] * n
ptr = 1

def dfs(g, seen, idx):
    global first_order, first_order, ptr

    first_order[idx] = ptr
    ptr += 1

    seen[idx] = True
    for i in g[idx]:
        # idxから行ける各頂点について
        if seen[i]: continue
        dfs(g, seen, i)

    last_order[idx] = ptr
    ptr += 1

seen = [False] * n
dfs(g, seen, 0)

# 孤立している頂点対策
for i in range(n):
    if not seen[i]:
        ans = dfs(g, seen, i)

# 出力
for idx, (f, l) in enumerate(zip(first_order, last_order)):
    print(idx+1, f, l)
