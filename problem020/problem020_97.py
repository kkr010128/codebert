from collections import deque


deq = deque()
n = int(input())
for _ in range(n):
    operation = input()
    if operation == "deleteFirst":
        deq.popleft()
    elif operation == "deleteLast":
        deq.pop()
    
    else:
        command, value = operation.split()
        if command == "insert":
            deq.appendleft(int(value))
        elif command == "delete":
            try:
                deq.remove(int(value))
            except ValueError:
                pass

print(*deq)

