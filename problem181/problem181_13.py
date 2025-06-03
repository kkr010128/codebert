from collections import deque

K = int(input())
q = deque([])
if K < 10:
    print(K)
    exit()
for i in range(1, 10):
    q.append(i)
counter = 9
while counter < K:
    tmp = q.popleft()
    f = tmp%10
    tmp = tmp * 10
    if f == 0:
        q.append(tmp)
        q.append(tmp+1)
        counter += 2
    elif f == 9:
        q.append(tmp+f-1)
        q.append(tmp+f)
        counter += 2
    else:
        q.append(tmp+f-1)
        q.append(tmp+f)
        q.append(tmp+f+1)
        counter += 3
for i in range(K, counter):
    q.pop()
print(q.pop())