import sys
from collections import defaultdict
from queue import Queue


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    g = defaultdict(list)
    for i in range(n):
        line = list(map(int, input().split()))
        if line[1] > 0:
            g[line[0]] = line[2:]
    q = Queue()
    q.put(1)
    dist = [-1] * (n + 1)
    dist[1] = 0
    while not q.empty():
        p = q.get()
        for nxt in g[p]:
            if dist[nxt] == -1:
                dist[nxt] = dist[p] + 1
                q.put(nxt)
    for i in range(1, n + 1):
        print(i, dist[i])


if __name__ == "__main__":
    main()

