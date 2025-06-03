from collections import deque
k = int(input())
d = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

for i in range(k - 1):
    x = d.popleft()
    if x%10 > 0:
        d.append(x*10 + x%10 - 1)
    d.append(x*10 + x%10)
    if x%10 < 9:
        d.append(x*10 + x%10 + 1)

print(d.popleft())