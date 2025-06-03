from collections import deque
K = int(input())

q = [1, 2, 3, 4, 5, 6, 7, 8, 9]
q = deque(q)

def next_n(n):
    if n == 0:
        return [0, 1]
    elif n == 9:
        return [8, 9]
    else:
        return [n-1, n, n+1]

for _ in range(K-1):
    now = q.popleft()
    for next_ in next_n(now%10):
        q.append(now*10 + next_)

print(q[0])