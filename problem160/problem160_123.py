from collections import deque
N, M, Q = map(int, input().split())
I = [list(map(int, input().split())) for _ in range(Q)]

que = deque()
ans = 0
for i in range(1, M+1):
    que.append([i])

while que:
    seq = que.popleft()
    
    if len(seq) == N:
        p = 0
        for i in range(Q):
            if seq[I[i][1]-1] - seq[I[i][0]-1] == I[i][2]:
                p += I[i][3]
        ans = max(ans, p)
    else:
        for i in range(seq[-1], M+1):
            seq_next = seq + [i]
            que.append(seq_next)

print(ans)