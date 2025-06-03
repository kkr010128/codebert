from collections import deque

n, q = map(int, input().split())
queue = deque([])
for i in range(n):
    a = input().split()
    queue.append([a[0], int(a[1])])

time = 0

while queue:
    b = queue.popleft()
    if b[1] <= q:
        time += b[1]
        print(b[0] + ' ' + str(time))
    else:
        b[1] -= q
        time += q
        queue.append(b)