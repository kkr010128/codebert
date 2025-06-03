import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

from collections import deque,defaultdict,Counter
def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for i in range(N):
        A = list(map(int,input().split()))
        for a in A[2:]:
            a -= 1
            G[i].append(a)
    
    q = deque([0])
    dist = [-1] * N
    dist[0] = 0
    while q:
        v = q.popleft()
        for e in G[v]:
            if dist[e] >= 0:
                continue
            dist[e] = dist[v] + 1
            q.append(e)
    
    ans = [(i + 1,dist[i]) for i in range(N)]
    for t in ans:
        print(*t)
if __name__ == '__main__':
    main()
