from collections import deque

n, q = map(int, input().split())
dq = deque()

for _ in range(n):
    name, time = input().split()
    dq.append([name, int(time)])

cnt = 0

while dq:
    qt = dq.popleft()
    if qt[1] <= q:
        cnt += qt[1]
        print(qt[0], cnt)
    else:
        cnt += q
        qt[1] -= q
        dq.append(qt)