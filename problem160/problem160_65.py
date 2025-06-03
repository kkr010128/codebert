n, m, q = list(map(int, input().split()))
from collections import deque
ans = 0
def calc(seq):
    score = 0
    for a, b, c, d in req:
        if seq[b-1] - seq[a-1] == c:
            score+= d
    return score
req = [list(map(int, input().split())) for i in range(q)]

que = deque()

for h in range(1, m+1):
    que.append([h])

while que:
    seq = que.popleft()
    if len(seq) == n:
        score = calc(seq)
        ans = max(ans, score)
    else:
        for i in range(seq[-1], m+1):
            seq_next = seq + [i]
            que.append(seq_next)

print(ans)