import collections

k = int(input())
Q = collections.deque([int(i) for i in range(1, 10)])
for _ in range(k):
    x = Q.popleft()
    if x%10:
        Q.append(10*x + x%10 - 1)
    Q.append(10*x + x%10)
    if x%10 != 9:
        Q.append(10*x + x%10 + 1)
print(x)
