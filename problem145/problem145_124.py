#!/usr/bin/env python3
def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    N, M = map(int, input().split())
    G = [[] for _ in [0] * (N + 1)]
    for _ in [0] * M:
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    
    q = deque([1])
    depth = [0 for _ in [0] * (N + 1)]
    while q:
        v = q.popleft()
        for nv in G[v]:
            if depth[nv] == 0:
                # depth[nv] = depth[v] + 1
                depth[nv] = v
                q.append(nv)
    if 0 in depth[2:]:
        print('No')
        return
    else:
        print('Yes')
        for guide in depth[2:]:
            print(guide)


if __name__ == '__main__':
    main()
