import collections

k = int(input())
Q = collections.deque([int(i) for i in range(1, 10)])
chk = False
for i in range(k):
    x = Q.popleft()
    if i + len(Q) > k:
        chk = True
    if chk:
        continue
    else:
        if x%10:
            Q.append(10*x + x%10 - 1)
        Q.append(10*x + x%10)
        if x%10 != 9:
            Q.append(10*x + x%10 + 1)
print(x)
