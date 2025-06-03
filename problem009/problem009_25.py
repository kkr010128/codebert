from collections import deque
n = int(input())
G = []
for _ in range(n):
    u, k, *v = map(int, input().split())
    u -= 1
    G.append(v)
q = deque()
seen = [False] * n
dist = [-1] * n

def main():
    q.append(0)
    seen[0] = True
    dist[0] = 0
    while len(q) > 0:
        now_v = q.popleft()
        for new_v in G[now_v]:
            new_v -= 1
            if seen[new_v] is True:
                continue
            seen[new_v] = True
            q.append(new_v)
#             print(now_v, new_v)
            dist[new_v] = dist[now_v] + 1
    
    for i in range(n):
        print(i+1, dist[i])

if __name__ == '__main__':
    main()
