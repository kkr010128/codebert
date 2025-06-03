from collections import deque
query = int(input())
l = deque()
for _ in range(query):
    command = input().strip()
    if command == "deleteFirst":
        try:
            l.popleft()
        except:
            pass
    elif command == "deleteLast":
        try:
            l.pop()
        except:
            pass
    else:
        command, value = command.split(" ")
        if command == "insert":
            l.appendleft(int(value))
        elif command == "delete":
            try:
                l.remove(int(value))
            except:
                pass
print(*l)