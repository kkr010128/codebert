from collections import deque

H, W = map(int, input().split())
field = ['#' * (W+2)] * (H+2)
for i in range(1, H+1):
    field[i] = '#' + input() + '#'
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
ans = 0
q = deque()

for si in range(1, H+1):
    for sj in range(1, W+1):
        if field[si][sj] == '#':
            continue
        q.clear()
        q.append([si, sj])
        dist = [[-1 for _ in range(W+2)] for _ in range(H+2)]
        dist[si][sj] = 0
        dist_max = 0
        while len(q) != 0:
            current = q.popleft()
            ci = current[0]
            cj = current[1]

            for d in range(4):
                next_i = ci + di[d]
                next_j = cj + dj[d]

                if field[next_i][next_j] == '#':
                    continue

                if dist[next_i][next_j] != -1:
                    continue

                q.append([next_i, next_j])
                dist[next_i][next_j] = dist[ci][cj] + 1
                dist_max = max(dist_max, dist[next_i][next_j])
        ans = max(ans, dist_max)
print(ans)
