from collections import deque
K = int(input())
q = deque()
for i in range(1, 10):
    q.append(i)
i = 0
run = []
while i < K:
    i += 1
    x = q.popleft()
    if x % 10 != 0:
        q.append(10*x + x%10 - 1)
    q.append(10*x + x%10)
    if x % 10 != 9:
        q.append(10*x + x%10 + 1)
    run.append(x)

print(run[K - 1])
