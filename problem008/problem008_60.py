import sys
from collections import defaultdict


time = 1


def dfs(g, visited, start, ans):
    global time
    visited[start - 1] = True
    ans[start - 1][0] = time
    for e in g[start]:
        if not visited[e - 1]:
            time += 1
            dfs(g, visited, e, ans)
    time += 1
    ans[start - 1][1] = time


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    g = defaultdict(list)
    for i in range(n):
        line = list(map(int, input().split()))
        if line[1] > 0:
            g[line[0]] = line[2:]
    visited = [False] * n

    ans = [[1, 1] for _ in range(n)]
    global time
    while False in visited:
        start = visited.index(False) + 1
        dfs(g, visited, start, ans)
        time += 1

    for i in range(1, n + 1):
        print(i, *ans[i - 1])


if __name__ == "__main__":
    main()

