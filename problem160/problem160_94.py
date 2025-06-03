from collections import deque
N, M, Q = map(int, input().split())
A = [list(map(int, input().split())) for i in range(Q)]

def calc(x):
    ans = 0
    for a, b, c, d in A:
        if int(x[b-1]) - int(x[a-1]) == c:
            ans += d
    return ans

q = deque([[1]])
ans = 0
while q:
    tmp = q.popleft()
    if len(tmp) == N:
        ans = max(ans, calc(tmp))
    else:
        for i in range(tmp[-1], M+1):
            q.append(tmp+[i])

print(ans)