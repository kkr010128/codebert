from collections import deque
a = deque([])
for i in range(int(input())):
    c = input().split()
    if c[0] == "insert":
        a.appendleft(c[1])
    elif c[0] == "delete":
        try:
            a.remove(c[1])
        except ValueError:
            pass
    elif c[0] == "deleteFirst":
        a.popleft()
    else:
        a.pop()
for i,e in enumerate(a):
    if i == len(a) - 1:
        print(e)
    else:
        print(e, end=" ")

