#!/usr/bin/env python3
def main():
    import sys

    input = sys.stdin.readline

    N, M = map(int, input().split())
    H = [0] + [int(x) for x in input().split()]
    graph = [[] for _ in [0] * (N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    res = N
    for i in range(1, N + 1):
        if graph[i]:
            for j in graph[i]:
                if H[j] >= H[i]:
                    res -= 1
                    break
    print(res)


if __name__ == '__main__':
    main()
