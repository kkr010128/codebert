from collections import deque
d = deque()
for a in range(int(input())):
    com = input().split()
    if com[0] == "insert":
        d.appendleft(com[1])
    elif com[0] == "delete":
        if com[1] in d:
            d.remove(com[1])
    elif com[0] == "deleteFirst":
        d.popleft()
    elif com[0] == "deleteLast":
        d.pop()
    else:
        break
print(*d)

