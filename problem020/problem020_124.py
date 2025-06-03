from collections import deque

N = int(input())

d = deque([])
for i in range(N):
    a = input()
    if a == "deleteFirst":
        d.popleft()
    elif a == "deleteLast":
        d.pop()
    else:
        a, b = a.split()
        if a == "insert":
            d.appendleft(b)
        else:
            try:
                d.remove(b)
            except:
                pass

print(*d)
