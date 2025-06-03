from collections import deque


k = int(input())
num_deq = deque([i for i in range(1, 10)])
for i in range(k-1):
    x = num_deq.popleft()
    if x % 10 != 0:
        num_deq.append(10 * x + x % 10 - 1)
    num_deq.append(10 * x + x % 10)
    if x % 10 != 9:
        num_deq.append(10 * x + x % 10 + 1)
x = num_deq.popleft()
print(x)
