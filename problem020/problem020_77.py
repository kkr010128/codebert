from collections import deque
n = int(input())
l = deque()
for _ in range (n):
    cmd = input().split(' ')
    if cmd[0]=='insert':
        l.appendleft(cmd[1])  
    if cmd[0]=='delete':
        try:l.remove(cmd[1])
        except :pass
    if cmd[0]=='deleteFirst':
        l.popleft()
    if cmd[0]=='deleteLast':
        l.pop()
print(*l)

