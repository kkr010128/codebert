from collections import deque

n = int(input())
dll = deque([])

for _ in range(n):
    p = input().split()

    if   p[0] == "insert":
        dll.appendleft(p[1])

    elif p[0] == "delete":
        try:
            dll.remove(p[1])
        except:
            pass

    elif p[0] == "deleteFirst":
        dll.popleft()

    else:
        dll.pop()

print(" ".join(dll))
