from collections import defaultdict

def main():
    N, M = map(int, input().split())
    g = defaultdict(set)

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1 
        g[a].add(b)
        g[b].add(a)

    def dfs(u, visited: set):
        stack = [u]
        visited.add(u)
        while stack:
            u = stack.pop()
            for v in g[u]:
                if v not in visited:
                    stack.append(v)
                    visited.add(v)

    count = dict()       
    for u in range(N):
        if u in count:
            continue
        visited = set()
        dfs(u, visited)
        # print(visited)
        count[u] = len(visited)
        for v in visited:
            count[v] = len(visited)

    print(max(count.values()))


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10000)
    main()