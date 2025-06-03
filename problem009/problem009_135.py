from collections import deque


def main():
    while que:
        v, d = que.popleft()
        for nv in G[v]:
            nv -= 1
            if D[nv] == -1:
                D[nv] = D[v] + 1
                que.append((nv, D[nv]))
    for i in range(N):
        print(i+1, D[i])


if __name__ == "__main__":
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N):
        ipts = [int(ipt) for ipt in input().split()]
        G[ipts[0]-1] = ipts[2:]
    D = [-1]*N
    D[0] = 0
    que = deque()
    que.append((0, 0))
    main()
