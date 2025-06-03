from collections import deque

k = int(input())

lunlun = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

for i in range(k):
    s = lunlun.popleft()
    
    if s % 10 != 0:
        lunlun.append(10 * s + s % 10 - 1)
    lunlun.append(10 * s + s % 10)
    if s % 10 != 9:
        lunlun.append(10 * s + s % 10 + 1)

print(s)
