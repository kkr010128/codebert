from collections import deque

K = int(input())
Q = deque()
for i in range(1, 10):
    Q.append(i)
temp = 0
for i in range(K):
    temp = Q.popleft()
    if temp%10 != 0:
        Q.append(temp*10+temp%10-1)
    Q.append(temp*10+temp%10)
    if temp%10 != 9:
        Q.append(temp*10+temp%10+1)
print(temp)