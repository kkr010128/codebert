from collections import deque

k = int(input())

num = deque()
num = deque([i for i in range(1,10)])

for i in range(k):
    x = num.popleft()
    mod = x % 10
    if x % 10 != 0:
        num.append(10*x + mod-1)
    num.append(10*x + mod)
    if x % 10 != 9:
        num.append(10*x + mod+1)
print(x)