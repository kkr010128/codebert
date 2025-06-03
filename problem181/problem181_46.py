from collections import deque

k = int(input())
q = deque([])
for i in range(1, 10):
    q.append(i)

cnt = 0
while cnt < k:
    s = q.popleft()
    cnt += 1
    t = s % 10
    if t != 0:
        q.append(10 * s + (t - 1))
    q.append(10 * s + t)
    if t != 9:
        q.append(10 * s + (t + 1))
    
print(s)
        
