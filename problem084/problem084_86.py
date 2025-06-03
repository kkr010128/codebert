from collections import deque


def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    ans = 0
    visited = [False] * n

    for i in range(n):
        if visited[i]:
            continue

        q = deque()
        q.append(i)
        cnt = 1
        visited[i] = True

        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    q.append(v)
                    cnt += 1
                    visited[v] = True
            ans = max(ans, cnt)

    print(ans)


if __name__ == "__main__":
    main()
