from collections import deque

N, M = list(map(int, input().split()))

# N個の空の配列
# g[0]は空のまま
path_list = [[] for i in range(N + 1)]

# 繋がっている部屋をメモ
for i in range(M):
    a, b = list(map(int, input().split()))
    path_list[a].append(b)
    path_list[b].append(a)

queue = deque([1])
d = [None] * (N + 1)

while queue:
    # popleft()で先頭の要素を返しつつ削除
    v = queue.popleft()
    # vから行ける全ての部屋について
    for i in path_list[v]:
        if d[i] is None:
            d[i] = v
            queue.append(i)

print("Yes")
# 2番以降の部屋について
for i in d[2:]:
    print(i)
