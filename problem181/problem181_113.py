from collections import deque
def bfs(k):
    lunlun = []
    q = deque()
    count = 0
    for i in range(1, 10):
        lunlun.append(i)
        q.append(i)
        count += 1

    if count >= k:return lunlun[k - 1]

    while True:
        num = q.popleft()
        tail = num % 10
        for i in [-1, 0, 1]:
            temp = tail + i
            if temp == -1 or temp == 10:continue
            q.append(num * 10 + temp)
            lunlun.append(num * 10 + temp)
            count += 1
            if k == count:return lunlun[k - 1]

k = int(input())
print(bfs(k))
