from collections import deque

def main():
    H, W = map(int, input().split())
    field = "#"*(W+2)
    field += "#" + "##".join([input() for _ in range(H)]) + "#"
    field += "#"*(W+2)

    INF = 10**9
    cost = [INF]*len(field)
    move = [-1, 1, -(W+2), W+2]
    def bfs(s, g):
        q = deque()
        dequeue = q.popleft
        enqueue = q.append
        cost[s] = 0
        enqueue(s)

        while q:
            now = dequeue()
            now_cost = cost[now]
            for dx in move:
                nv = now + dx
                if nv == g:
                    cost[g] = now_cost + 1
                    return
                if field[nv] == "#" or cost[nv] < INF:
                    continue
                else:
                    cost[nv] = now_cost + 1
                    q.append(nv)
    
    ans = 0
    for si in range(H):
        for sj in range(W):
            for gi in range(H):
                for gj in range(W):
                    start = (si+1)*(W+2)+sj+1
                    goal = (gi+1)*(W+2)+gj+1
                    if field[start] == "#" or  field[goal] == "#" or start == goal:
                        continue
                    cost = [INF] * len(field)
                    bfs(start, goal)
                    ans = max(ans, cost[goal])
    print(ans)

if __name__ == "__main__":
    main()