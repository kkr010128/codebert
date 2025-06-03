from collections import deque

def main():
    n = int(input())
    _next = [[] for _ in range(n)]
    for _ in range(n):
        u, k, *v = map(lambda s: int(s) - 1, input().split())
        _next[u] = v
    queue = deque()
    queue.append(0)
    d = [-1] * n
    d[0] = 0
    while queue:
        u = queue.popleft()
        for v in _next[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                queue.append(v)
    for i, v in enumerate(d, start=1):
        print(i, v)


if __name__ == '__main__':
    main()

