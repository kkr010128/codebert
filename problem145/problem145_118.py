from collections import deque


def solve():
    N, M = map(int, input().split())
    to = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        to[a].append(b)
        to[b].append(a)

    que = deque()
    hint = [0] * N
    seen = [False] * N

    seen[0] = True
    que.appendleft(0)

    # BFS
    while que:
        v = que.popleft()
        for nv in to[v]:
            if seen[nv]:
                continue
            que.append(nv)
            hint[nv] = v + 1
            seen[nv] = True

    print("Yes")
    print(*hint[1:], sep='\n')
    

if __name__ == "__main__":
    solve()
