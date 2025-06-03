from collections import deque

k = int(input())
q = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

cnt = 0
while q:
    curr = q.popleft()
    cnt += 1
    if cnt == k:
        break
    if curr % 10 == 9:
        q.append(curr * 10 + curr % 10 - 1)
        q.append(curr * 10 + curr % 10)
    elif curr % 10 == 0:
        q.append(curr * 10 + curr % 10)
        q.append(curr * 10 + curr % 10 + 1)
    else:
        q.append(curr * 10 + curr % 10 - 1)
        q.append(curr * 10 + curr % 10)
        q.append(curr * 10 + curr % 10 + 1)

print(curr)