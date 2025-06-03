from collections import deque
n = int(input())
l = deque()
for i in range(n):
    s = input()
    l.append(s)
print(len(set(l)))