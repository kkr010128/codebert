from collections import deque

n = int(input())

l = deque()
for _ in range(n):
    command = input().split()
    if command[0] == "insert":
        l.appendleft(command[1])
    elif command[0] == "delete":
        try:
            ind = l.remove(command[1])
        except ValueError:
            pass
    elif command[0] == "deleteFirst":
        l.popleft()
    elif command[0] == "deleteLast":
        l.pop()
        
print (" ".join(l))