from collections import deque

n = int(input())
Q= deque()

for _ in range(n):
    str = input()
    if str == "deleteFirst":
        Q.popleft()
    elif str == "deleteLast":
        Q.pop()
    else:
        cmd,key = str.split()
        if cmd == "insert":
            Q.appendleft(key)
        elif cmd == "delete":
            try:
                Q.remove(key)
            except:
                pass
print(" ".join(list(Q)))
