from collections import deque


def bfs(g, source):
    n = len(g)
    d = [float('inf') for _ in range(n)]
    d[0] = 0
    queue = deque()
    queue.append(0)
    while len(queue) > 0:
        cur = queue.popleft()
        for next in g[cur]:
            if d[cur] + 1 < d[next]:
                d[next] = d[cur] + 1
                queue.append(next)
    return d


def main():
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n):
        inp = list(map(int, input().split()))
        m = inp[0] - 1
        k = inp[1]
        for i in range(k):
            g[m].append(inp[i+2] - 1)
    d = bfs(g, 0)
    for i in range(n):
        if d[i] == float('inf'):
            d[i] = -1
        print(i+1, d[i])


if __name__ == '__main__':
    main()

