from collections import deque, defaultdict


def main():
    N, X, Y = map(int, input().split())
    g = [[] for _ in range(N)]
    for i in range(N-1):
        g[i].append(i+1)
        g[i+1].append(i)
    g[X-1].append(Y-1)
    g[Y-1].append(X-1)
    ans = defaultdict(int)

    for i in range(N):
        q = deque()
        q.append(i)
        visit_time = [0 for _ in range(N)]
        while len(q):
            v = q.popleft()
            time = visit_time[v]
            for j in g[v]:
                if visit_time[j] == 0 and j != i:
                    q.append(j)
                    visit_time[j] = time + 1
                else:
                    visit_time[j] = min(time + 1, visit_time[j])

        for v in visit_time:
            ans[v] += 1

    for i in range(1, N):
        print(ans[i] // 2)


if __name__ == '__main__':
    main()
