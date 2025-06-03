from collections import defaultdict


def dfs(N, tree, v):
    s = []
    done = [False for _ in range(N)]
    dist = [0 for _ in range(N)]

    done[v] = True
    dist[v] = 0
    s.append(v)

    while 0 < len(s):
        v = s.pop()

        # process
        # print(v, tree[v], dist[v])

        for i in tree[v]:
            if not done[i]:
                done[i] = True
                dist[i] = dist[v] + 1
                s.append(i)

    return dist


def main():
    N, u, v = map(int, input().split())
    u -= 1
    v -= 1

    tree = defaultdict(list)

    for _ in range(N - 1):
        A, B = map(int, input().split())
        A -= 1
        B -= 1

        tree[A].append(B)
        tree[B].append(A)

    u_dist = dfs(N, tree, u)
    v_dist = dfs(N, tree, v)
    # print(u_dist)
    # print(v_dist)

    ans = 0
    for u1, v1 in zip(u_dist, v_dist):
        if u1 < v1:
            ans = max(ans, v1 - 1)

    print(ans)


main()
