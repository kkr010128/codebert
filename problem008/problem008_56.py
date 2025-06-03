# -*- coding:utf-8 -*-

def solve():
    from collections import deque

    N = int(input())
    Us = [[] for _ in range(N)]

    for i in range(N):
        _in = list(map(int, input().split()))
        if len(_in) == 2:
            continue
        u, k, Vs = _in[0], _in[1], _in[2:]
        Vs.sort()
        for v in Vs:
            Us[u-1].append(v-1)
        Us[u-1] = deque(Us[u-1])

    find = [0 for _ in range(N)]  # 発見時刻
    terminated = [0 for _ in range(N)]  # 終了時刻
    tim = [0]  # 経過時間

    def dfs(now):
        while Us[now]:
            nxt = Us[now].popleft()

            if find[nxt] != 0:
                continue

            tim[0] += 1
            find[nxt] = tim[0]

            dfs(nxt)

        if terminated[now] == 0:
            tim[0] += 1
            terminated[now] = tim[0]

    for i in range(N):
        if find[i] == 0:
            tim[0] += 1
            find[i] = tim[0]
            dfs(i)

    for i in range(N):
        print(i+1, find[i], terminated[i])


if __name__ == "__main__":
    solve()

