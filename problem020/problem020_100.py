from collections import deque
dq = deque()
for _ in [None]*int(input()):
    s = input()
    if s == "deleteFirst":
        dq.popleft()
    elif s == "deleteLast":
        dq.pop()
    else:
        a, b = s.split()
        if a == "insert":
            dq.appendleft(b)
        else:
            if b in dq:
                dq.remove(b)
print(" ".join(dq))

