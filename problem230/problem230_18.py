import heapq

N, D, A = map(int, input().split(" "))
proc_que = []

for _ in range(N):
    x, h = map(int, input().split(" "))
    heapq.heappush(proc_que, (x, h))

damaged = 0
ans = 0

while len(proc_que) > 0:
    x, h = heapq.heappop(proc_que)
    if h > 0:
        # monster
        num_bomb_use = max(0, (h - damaged + A - 1) // A)
        ans += num_bomb_use
        damaged += num_bomb_use * A
        heapq.heappush(proc_que, (x + 2 * D + 1, -num_bomb_use * A))
    else:
        # damaged end
        damaged += h

print(ans)