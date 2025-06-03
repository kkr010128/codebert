import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from collections import deque
from copy import deepcopy
def main():
    n, m = map(int, input().split())
    edges = {e:[] for e in range(n + 1)}
    for _ in range(m):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)

    res = [0] * (n + 1)
    dist = 1
    distroom = [n + 1] * (n + 1)
    distroom[1] = 0
    q1 = deque()
    q2 = deque()
    q1.append(1)
    while q1:
        for q1e in q1:
            for adj in edges[q1e]:
                if distroom[adj] > dist:
                    res[adj] = q1e
                    distroom[adj] = dist
                    q2.append(adj)
        dist += 1
        q1 = deepcopy(q2)
        q2 = deque()
    print('Yes')
    print(*res[2:],sep='\n')

if __name__ == '__main__':
    main()